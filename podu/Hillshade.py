# 山体阴影
import sys
from qgis.analysis import QgsNativeAlgorithms
from qgis.core import QgsApplication

sys.path.append(r"D:\Tools\QGIS 3.16.11\apps\qgis-ltr\python\plugins")

import processing
from processing.core.Processing import Processing

from qgis._core import QgsRasterLayer
from qgis.utils import iface

qgs = QgsApplication([], False)
qgs.initQgis()

Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())


# qgs.exitQgis()

parameter_dictionary = {'AZIMUTH': 300,
                        'INPUT': 'D:/Desktop/pointTest/dem.tif',
                        'OUTPUT': 'D:/Desktop/pointTest/山体阴影.tif',
                        'V_ANGLE': 40,
                        'Z_FACTOR': 1}
processing.run("qgis:hillshade", parameter_dictionary)
path_to_tif = "D:/Desktop/pointTest/山体阴影.tif"
# vlayer = QgsRasterLayer(path_to_tif, "山体阴影")
# iface.addRasterLayer(path_to_tif, "山体阴影")
qgs.exitQgis()