import arcpy as ap

fc = 'C:/lod2/LOD2_Gehrden_roof.shp'
fields = ["SHAPE@", "GEBID", "NAME"]
fields2 = ["NAME", "DACHINF"]
'''
with ap.da.UpdateCursor(fc, fields) as cursor:
    gebid=""
    for row in cursor:
        if row[1]==gebid:
            row[2]="notRoof"
        else:
            gebid=row[1]
            row[2]="Roof"
        cursor.updateRow(row)
        #print(row)
'''
'''
with ap.da.UpdateCursor(fc, fields2) as cursor:
    for row in cursor:
        if row[0] == "Roof":
            row[1] = 1
        else:
            row[1] = 0
        cursor.updateRow(row)
'''
# ap.env.workspace = r"C:\LOD2"
# ap.Dissolve_management("LOD2_Gehrden_merge_selection.shp", "LODmerged", "GEBID")
# desc = ap.Describe("LOD2_Gehrden_merge_selection.shp")
# print(desc.shapeType)
