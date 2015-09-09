from qgis.core import *
import networkx as nx

data_source = '/Users/laurensversluis/Google Drive/PyQGIS/Project/SSx_Toolkit/Data/Lines.shp'

layer = QgsVectorLayer(data_source, 'input', 'ogr')
if not layer.isValid():
    print 'Layer is not valid!'

G = nx.read_shp(data_source)

network = nx.Graph()



for e in G.edges_iter():
    e1 = e[0]
    e2 = e[1]
    p1 = QgsGeometry.fromWkt('Point(e1[0],e1[1])')
    p2 = QgsGeometry.fromWkt('Point(e2[0],e2[1])')
    d = QgsDistanceArea()
    d.setEllipsoidalMode(True)
    network.add_edge(e1,e2,weight=d.measureLine(QgsPoint(e1[0],e1[1]),QgsPoint(e2[0],e2[1])))

for e in network.edges_iter():
    print e

#for e in network.edges_iter():
 #   nx.single_source_dijkstra_path_length(G,origin,e,weight='weight')
