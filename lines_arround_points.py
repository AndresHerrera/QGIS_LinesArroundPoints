# -*- coding: utf-8 -*-
"""
/***************************************************************************
 lines_arround_points
 Creates lines arround a point layer given length and segments
        -------------------
        begin                : 2020-01-10
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Andres Herrera
        email                : t763rm3n@gmail.com
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 """
import sys
import math 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# configure input and output layers
layerPoints = 'mypoints'
outpuLayer = 'linesoutput'

# let's access the 'mypoints' layer
pointLayer = QgsProject.instance().mapLayersByName(layerPoints)[0]
pointFeatures = pointLayer.getFeatures(QgsFeatureRequest())

# create a new memory layer
# set the right crs
lineOutputLayer = QgsVectorLayer("LineString?crs=EPSG:3115", outpuLayer, "memory")
pr = lineOutputLayer.dataProvider()

def createLineFeatureAroundPoint(x,y,distance,segments):
    lineStart = QgsPoint(x,y)
    steps=int(360/segments)
    for n in range(0,360,steps):
        alpha = (n * math.pi) / 180
        xx = x + (distance * math.cos(alpha))
        yy = y + (distance * math.sin(alpha))
        lineEnd = QgsPoint(xx,yy)   
        # create a new feature
        seg = QgsFeature()
        # add the geometry to the feature, 
        seg.setGeometry(QgsGeometry.fromPolyline([lineStart, lineEnd]))
        # add the geometry to the layer
        pr.addFeatures( [ seg ] )

# now loop through the features, perform geometry computation and create the lines
for f in pointFeatures:
  geom = f.geometry()
  x = geom.asPoint().x()
  y = geom.asPoint().y()
  createLineFeatureAroundPoint(x,y,100,8)
  
# update extent of the layer (not necessary)
lineOutputLayer.updateExtents()  
# show the line  
QgsProject.instance().addMapLayer(lineOutputLayer)  




