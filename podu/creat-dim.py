import processing
import os # This is is needed in the pyqgis console also
from qgis.core import (
    QgsVectorLayer
)
from qgis.core import (
    QgsRasterLayer
)
from qgis.utils import iface

#用z坐标插值
parameter_dictionary = {'DISTANCE_COEFFICIENT': 2,
                        'EXTENT': '119.316549319,119.349260171,25.991966726,26.000361547 [EPSG:4326]',
                        'INTERPOLATION_DATA' : 'file:///D:/Desktop/mycsv.csv?delimiter=,&crs=epsg:4326&xField=lat&yField=lon&zField=value::~::1::~::-1::~::0',
                        'OUTPUT': 'D:/Desktop/pointTest/dem.tif',
                        'PIXEL_SIZE': 4.2e-05}

processing.run("qgis:idwinterpolation", parameter_dictionary)


path_to_tif = "D:/Desktop/pointTest/dem.tif"
vlayer = QgsRasterLayer(path_to_tif, "dem地形")
iface.addRasterLayer(path_to_tif, "dem地形")
