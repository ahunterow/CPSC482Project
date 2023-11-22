# Driver for testing the quad tree.

import treelib as tl

from QNode import *
from NDNode import *

# Constants for search_region's initial call. These are just relative to the data we are using for the example.
MAXLEFT = -10
MAXRIGHT = 10
MAXUP = 10
MAXDOWN = -10

# root
qtree = NDNode((0, 0, 0))

# Test data for a quad tree
qtree.insert((-5,7,0))
qtree.insert((-3,-4,1))
qtree.insert((-4,4,0))
qtree.insert((4,3,1))
qtree.insert((8,-6,0))
qtree.insert((-9,6,1))
qtree.insert((3,-2,0))
qtree.insert((6,7,1))
qtree.insert((8,2,0))
qtree.insert((4,-7,1))
qtree.insert((-7,-8,0))

# Deletion tests
# print(qtree.delete((0, 0, 0)))
# print(qtree.delete((-5, 7, 0)))
# print(qtree.delete((8, -6, 0)))
# print(qtree.delete((-3, -4, 1)))

# Output to file
tree = qtree.tree_build()
tree.save2file("qtreeTest")

# Test the region searching
nodes = []
print("First")
qtree.search_region(nodes, [(2, 9), (-3, 4),(0,0)], [(MAXDOWN, MAXUP), (MAXDOWN, MAXUP), (MAXDOWN, MAXUP)])
for node in nodes:
    print(node.point)
nodes.clear()
print("Second")
qtree.search_region(nodes, [(-6, -2), (3, 8),(0,0)], [(MAXDOWN, MAXUP), (MAXDOWN, MAXUP), (MAXDOWN, MAXUP)])
for node in nodes:
    print(node.point)
nodes.clear()
print("Third")
qtree.search_region(nodes, [(-3, 8), (-7, 4),(0,0)], [(MAXDOWN, MAXUP), (MAXDOWN, MAXUP), (MAXDOWN, MAXUP)])
for node in nodes:
    print(node.point)
nodes.clear()

