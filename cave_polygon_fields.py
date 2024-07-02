#===========================================================
#===========================================================
#Add fields to cave polygon layer
#(floor, ceiling, height, area, volume)
#Lin Yangchen
#29 June 2024
#===========================================================
#===========================================================

#make sure the correct layer is selected in QGIS
#for distance accuracy, CRS should be EPSG:32650

#===========================================================

#iface for interacting with QGIS environment
#access the active layer
layer = iface.activeLayer()

#===========================================================

#add new fields
#types: String, Int, Double

layer.dataProvider().addAttributes([QgsField("FLOOR", QVariant.Double),
                  QgsField("CEILING", QVariant.Double),
                  QgsField("HEIGHT", QVariant.Double),
                  QgsField("AREA", QVariant.Double),
                  QgsField("VOLUME", QVariant.Double)])
                  
layer.updateFields()

#===========================================================

#QGIS expressions
floor = QgsExpression('ELEVATION - MEAN_DOWN')
ceiling = QgsExpression('ELEVATION + MEAN_UP')
height = QgsExpression('MEAN_DOWN + MEAN_UP')
area = QgsExpression('$area')
volume = QgsExpression('AREA * HEIGHT')

#context for executing expressions
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

#===========================================================

with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['FLOOR'] = floor.evaluate(context)
        f['CEILING'] = ceiling.evaluate(context)
        f['HEIGHT'] = height.evaluate(context)
        f['AREA'] = area.evaluate(context)
        layer.updateFeature(f)
        
with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['VOLUME'] = volume.evaluate(context)
        layer.updateFeature(f)
        









