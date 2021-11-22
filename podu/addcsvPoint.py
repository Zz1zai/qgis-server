#从csv文件添加点

import os

from qgis._core import QgsProject
from qgis.core import (
    QgsVectorLayer
)

uri = 'file:///D:/Desktop/mycsv.csv?delimiter={}&crs=epsg:4326&xField={}&yField={}&zField={}'.format(",", "lat", "lon", "value")
# uri = 'file:///D:/Saved Stuff/gulags/1.40.csv?delimiter=;&yField=y&xField=x'
print(uri)
vlayer = QgsVectorLayer(uri, "point", "delimitedtext")
QgsProject.instance().addMapLayer(vlayer)
