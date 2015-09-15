from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis import *
import networkx as nx


def run_script(iface):

    layer = iface.mapCanvas().currentLayer()

    if not layer.isValid():
        print 'Layer is not valid!'
        break

    else:

        G = nx.read_shp(layer)

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
