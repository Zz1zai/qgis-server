#加载矢量图层

import os
from qgis._core import QgsProject
from qgis.core import (
    QgsVectorLayer
)
# get the path to the shapefile e.g. /home/project/data/ports.shp

#配置矢量地址
path_to_airports_layer = "D:\Desktop\一级河流hyd1_4m\hyd1_4l.shp"

# The format is:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(path_to_airports_layer, "Airports layer", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)