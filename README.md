# QGIS_LinesArroundPoints

 Create lines arround a point layer given line length and number of the segments

## Requeriments

* QGIS 3.x
* Input point layer must be in meters - define the right CRS according to your data 
#### Run the script

* Open *lines_arround_points.py* script onto Python Console integrated in QGIS  ( Plugins-> Python Console )
* Open the point layer into QGIS environment
* Setup input and output layers
```python
# configure input and output layers
layerPoints = 'mypoints'
outpuLayer = 'linesoutput'
```

* Define line distance from point e.g. *100* : Distance in meters units
* Define number of segments e.g. *8*  : Creates lines each 45 degrees

```python
# configure input and output layers
createLineFeatureAroundPoint(x,y,100,8)
```

* Run the script

## Screenshot
![screenshot 1](https://github.com/AndresHerrera/QGIS_LinesArroundPoints/raw/master/screenshot.png "Screenshot")
