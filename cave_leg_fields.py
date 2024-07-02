#===========================================================
#===========================================================
#Add fields to cave leg layer
#(year of survey, 3D length, gradient, azimuth)
#Lin Yangchen
#30 June 2024
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

layer.dataProvider().addAttributes([QgsField("YEAR", QVariant.Int),
                  QgsField("LENGTH_3D", QVariant.Double),
                  QgsField("GRADIENT", QVariant.Double),
                  QgsField("AZIMUTH", QVariant.Double)])
                  
layer.updateFields()

#===========================================================

#QGIS expressions
year = QgsExpression('year(DATE1)')
length_3d = QgsExpression('length3D($geometry)')
gradient = QgsExpression('abs(z(start_point($geometry)) - z(end_point($geometry)))/$length')
azimuth = QgsExpression('degrees(azimuth(start_point($geometry), end_point($geometry)))')

#context for executing expressions
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

#===========================================================

with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['YEAR'] = year.evaluate(context)
        f['LENGTH_3D'] = length_3d.evaluate(context)
        f['GRADIENT'] = gradient.evaluate(context)
        f['AZIMUTH'] = azimuth.evaluate(context)
        layer.updateFeature(f)
        









