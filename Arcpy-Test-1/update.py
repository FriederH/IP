import zipfile
from arcgis.gis import GIS
import glob, os
import re

# Set wea height to 100 m using a cursor on the shapefile
# UpdateCursor sets a lock on the shp
shapefile = r"Z:\ArcGIS\0_Data\upload\wea_upload.shp"
fields = ["hoeheges", "anlagtyp"]


if 0:  # only used when a new shp is added
    import arcpy as ap

    with ap.da.UpdateCursor(shapefile, fields) as cursor:
        for row in cursor:
            rowAnlageTyp = row[1]
            x1 = re.findall("1", rowAnlageTyp)
            x2 = re.findall("2", rowAnlageTyp)
            if (x1) and not (x2):
                row[0] = 200
                cursor.updateRow(row)
            elif (x2) and not (x1):
                row[0] = 260
                cursor.updateRow(row)
            else:
                row[0] = 200  # Standardwert wenn nicht eingetragen ist
                cursor.updateRow(row)
        del row, cursor, ap

import arcpy as ap

# Delete existing zip-archives and lock-files in the upload directory
shapefileDir = r'Z:\ArcGIS\0_Data\upload'
os.chdir(shapefileDir)
for file in glob.glob('*.zip'):
    os.remove(file)
#for file in glob.glob('*.lock'):
#    os.remove(file)

nameTrunc = 'wea_upload*'
files = glob.glob(os.path.join(shapefileDir, nameTrunc))

# create zip archive with all the remaining files in the upload directory
with zipfile.ZipFile(os.path.join(shapefileDir, 'upload.zip'), 'w') as myzip:
    for file in files:
        name_file_only = file.split(os.sep)[-1]
        myzip.write(file, name_file_only)

# log in to gis
gis = GIS('home')  # build-in user with access to public LUH files

# prepare the upload of the zip archive, set parameters for the uploaded shapefile
dataPath = r"Z:\ArcGIS\0_Data\upload\upload.zip"
itemProps = {"snippet": "Manuell gesetzte WEAs in einer lokal erstellten SHP",
             "title": "WEAs",
             "tags": "wea",
             "type": "Shapefile",
             "overwrite": True,
             "access": "public"}

# overwrite an existing file
existingShapefile = gis.content.search(query="title:WEAs type:Shapefile owner:yue_z7f_luh_gis", item_type="Shapefile")[
    0]
existingShapefile.update(item_properties=itemProps, data=dataPath)

# search for existing feature layer
existingLayer = gis.content.search(query="title:upload", item_type="Feature Service")[0]

# deletion of existing feature layer
existingLayer.delete()

# publsih new shp as layer
shapefile_pub = existingShapefile.publish()
shapefile_pub.share(everyone=True)
