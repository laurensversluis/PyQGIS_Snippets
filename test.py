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

    p1 = QgsGeometry.fromPoint(QgsPoint(e1[0],e1[1]))
    p2 = QgsGeometry.fromPoint(QgsPoint(e2[0],e2[1]))

    d = QgsDistanceArea()
    d.setEllipsoidalMode(True)
    weight = d.measureLine(p1.asPoint(),p2.asPoint())
    print weight
    network.add_edge(e1,e2,weight='weight')

for e in network.edges_iter():

    print nx.single_source_dijkstra_path_length(G,e[0],cutoff=None,weight='weight')
