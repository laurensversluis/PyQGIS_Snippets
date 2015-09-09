# Customize this starter script by adding code
# to the run_script function. See the Help for
# complete information on how to create a script
# and use Script Runner.

""" Your Description of the script goes here """

# Some commonly used imports

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis import *
import networkx as nx


def run_script(iface):

    catchment = []
    r = 2000
    i = 0

    while i > len(cost):
        if cost < r:
            # next node
            if cost(next) < r:
                upperbound.append(i)
        i = i + 1

    G = nx.Graph() # creating an empty graph
    nx.read_shp(str(iface.activeLayer().source()))
    G.add_edge(1, 2, weight=4.7 )

    M = nx.single_source_shortest_path_length(G,0,)




    M = nx.ego_graph(G, (679980.26234586, 6059164.91455736), 1, center=True, undirected=False, distance=2000)
    nx.write_shp()

    layer = iface.mapCanvas().currentLayer()
    for f in layer.getFeatures():
        geom = f.geometry()
        G.add_node(geom)



((679980.26234586, 6059164.91455736), {})


