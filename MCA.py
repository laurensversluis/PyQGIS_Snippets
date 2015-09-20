from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis import *
import networkx as nx

""" Open network layer """

def run_script():

    nlayer = iface.activeLayer()
    iter = nlayer.getFeatures()
    G = nx.Graph()

    for f in iter:
        geom = f.geometry()
        if geom.wkbType() != QGis.WKBLineString:
            print "This is not a line layer."

        d = QgsDistanceArea()
        d.setEllipsoidalMode(True)

        weight = d.measureLine(geom.asPolyline())
        id= f.id()+1

        print id, '',weight

        p1 = geom.asPolyline()[0]

        p2 = geom.asPolyline()[1]
        print p1,p2
        G.add_edge(p1,p2,weight='weight')


#check if layer contains lines


run_script()
