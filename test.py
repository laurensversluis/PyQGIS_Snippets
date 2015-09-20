from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis import *
import networkx as nx


G = nx.read_shp("/Users/laurensversluis/Google Drive/PyQGIS/Project/SSx_Toolkit/Data/Lines.shp",simplify=True)

network = nx.Graph()

for e in G.edges_iter():

    e1 = e[0]
    e2 = e[1]
    print e1[0],e1[1]
    print e2[0],e2[1]

    p1 = QgsGeometry.fromPoint(QgsPoint(e1[0],e1[1]))
    p2 = QgsGeometry.fromPoint(QgsPoint(e2[0],e2[1]))

    d = QgsDistanceArea()
    d.setEllipsoidalMode(True)
    weight = d.measureLine(p1.asPoint(),p2.asPoint())
    print weight
    network.add_edge(e1,e2,weight=weight)

for e in network.edges_iter():

    print nx.single_source_dijkstra_path_length(G,e[0],cutoff=None,weight='weight')


"""
error = QgsVectorFileWriter.writeAsVectorFormat(layer, "my_shapes.shp", "CP1250", None, "ESRI Shapefile")

if error == QgsVectorFileWriter.NoError:
    print "success!"

#QgsVectorFileWriter"""