# 坡向分析
import sys

sys.path.append(r'D:\Tools\QGIS 3.16.11\apps\qgis-ltr\python\plugins')

import processing
# from processing.core.Processing import Processing
from qgis._core import QgsRasterLayer
from qgis.utils import iface

parameter_dictionary = {'INPUT': 'D:/Desktop/pointTest/dem.tif','OUTPUT' : 'D:/Desktop/pointTest/坡向3.tif','Z_FACTOR' : 1 }
print(processing)
processing.run("qgis:aspect", parameter_dictionary)
path_to_tif = "D:/Desktop/pointTest/坡向.tif"
vlayer = QgsRasterLayer(path_to_tif, "坡向分析")
iface.addRasterLayer(path_to_tif, "坡向分析")
