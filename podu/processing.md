qgis processing 插件使用

1.首先从从QGIS中导入QgsNativeAlgorithms和processing包，
值得注意的是processing是在python插件目录下，不是QGIS中的那个。
 ```buildoutcfg
from qgis.analysis import QgsNativeAlgorithms
from qgis.core import QgsApplication
sys.path.append(r"D:\Tools\QGIS 3.16.11\apps\qgis-ltr\python\plugins")
import processing
from processing.core.Processing import Processing
```
2.然后是初始化、调用和关闭：
```buildoutcfg
qgs = QgsApplication([], False)
qgs.initQgis()

Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
qgs.exitQgis()
```