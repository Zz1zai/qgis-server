# 坡度分析
import processing
from qgis._core import QgsRasterLayer
from qgis.utils import iface

parameter_dictionary = {'INPUT': 'D:/Desktop/pointTest/dem.tif',
                        'OUTPUT': 'D:/Desktop/pointTest/poudu.tif',
                        'Z_FACTOR': 2 }
processing.run("qgis:slope", parameter_dictionary)
path_to_tif = "D:/Desktop/pointTest/poudu.tif"
vlayer = QgsRasterLayer(path_to_tif, "坡度分析")
iface.addRasterLayer(path_to_tif, "坡度分析")
