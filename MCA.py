__author__ = 'laurensversluis'

##Network=vector
##Origins=point
##Radius=number 2000
##Results=output vector

import qgis
import networkx as nx

g = nx.read_shp('vector')

n = node
r = radius

nx.ego_graph(g,n,r,True,False,None)



