from arcgis.gis import GIS

# The code deletes a shapefile calles "WEAs" and a Feature Service published from the shapefile

# log in to gis
gis = GIS('home')  # build-in user with access to public files

# search for shapefile
existingShapefile = gis.content.search(query="title:WEAs type:Shapefile owner:yue_z7f_luh_gis", item_type="Shapefile")[0]

# deletion
existingShapefile.delete()

# search for feature layer
existingLayer = gis.content.search(query="title:upload", item_type ="Feature Service")[0]

# deletion
existingLayer.delete()