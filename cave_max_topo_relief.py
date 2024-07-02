#===========================================================
#===========================================================
#Find max topographic relief of a cave
#(gradient between lowest and highest stations)
#Lin Yangchen
#24 June 2024
#===========================================================
#===========================================================

#currently, script does not automatically exclude surface legs

#user settings

#make sure the correct layer is selected in QGIS
#for distance accuracy, CRS should be EPSG:32650

#change to the name of your elevation field
fieldname = 'ELEVATION'

#===========================================================

#iface for interacting with QGIS environment
#access the active layer
layer = iface.activeLayer()

#===========================================================

#field index (count starts from 0)
idx = layer.fields().indexFromName(fieldname)

#get min and max elevations
min = layer.minimumValue(idx)
max = layer.maximumValue(idx)

heightdiff = max - min
print(f'max depth = {heightdiff} m')

#===========================================================

#get coordinates

layer.selectByExpression(f"\"{fieldname}\" = '{min}'")
feature = layer.selectedFeatures()
point1 = feature[0].geometry().asPoint()

layer.selectByExpression(f"\"{fieldname}\" = '{max}'")
feature = layer.selectedFeatures()
point2 = feature[0].geometry().asPoint()

#get id of selected feature
#selected_id = layer.selectedFeatureIds()

#get feature by manually specifying id
#feature = layer.getFeature(509)

#get coordinates
#coords1 = [point1.x(), point1.y()]
#coords2 = [point2.x(), point2.y()]

#===========================================================

#2D distance between points
distance = point1.distance(point2)

#max relief of cave
slope = heightdiff/distance
print(f'max topographic relief = {slope}')

