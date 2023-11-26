# Driver for testing the quad tree.

import treelib as tl

from QNode import *
from NDNode import *

# Constants for search_region's initial call. These are just relative to the data we are using for the example.
MAXLEFT = -10
MAXRIGHT = 10
MAXUP = 10
MAXDOWN = -10

#
# NDNode Testing
#

# root
ndtree = NDNode((0, 0, 0))

# Test data for a quad tree
ndtree.insert((-5, 7, 0))
ndtree.insert((-3, -4, 1))
ndtree.insert((-4, 4, 0))
ndtree.insert((4, 3, 1))
ndtree.insert((8, -6, 0))
ndtree.insert((-9, 6, 1))
ndtree.insert((3, -2, 0))
ndtree.insert((6, 7, 1))
ndtree.insert((8, 2, 0))
ndtree.insert((4, -7, 1))
ndtree.insert((-7, -8, 0))

# Deletion tests
print("\nNDNode Delete Status:")
print(ndtree.delete((0, 0, 0))) # Should fail
print(ndtree.delete((-5, 7, 0)))
print(ndtree.delete((8, -6, 0)))
print(ndtree.delete((-3, -4, 1)))

# Output to file
tree = ndtree.tree_build()
tree.save2file("qtreeTest")

# Test the region searching
nodes = []
print("\nNDNode search_region tests:")
print("\nFirst search_region:")
ndtree.search_region(nodes, [(2, 9), (-3, 4), (0, 0)], [(MAXDOWN, MAXUP), (MAXDOWN, MAXUP), (MAXDOWN, MAXUP)])
for node in nodes:
    print(node.point)
nodes.clear()
print("\nSecond search_region:")
ndtree.search_region(nodes, [(-6, -2), (3, 8), (0, 0)], [(MAXDOWN, MAXUP), (MAXDOWN, MAXUP), (MAXDOWN, MAXUP)])
for node in nodes:
    print(node.point)
nodes.clear()
print("\nThird search_region:")
ndtree.search_region(nodes, [(-3, 8), (-7, 4), (0, 0)], [(MAXDOWN, MAXUP), (MAXDOWN, MAXUP), (MAXDOWN, MAXUP)])
for node in nodes:
    print(node.point)
nodes.clear()

#
# QNode Testing
#

qtree = QNode((0, 0))

# Test data for a quad tree
qtree.insert((-5, 7))
qtree.insert((-3, -4))
qtree.insert((-4, 4))
qtree.insert((4, 3))
qtree.insert((8, -6))
qtree.insert((-9, 6))
qtree.insert((3, -2))
qtree.insert((6, 7))
qtree.insert((8, 2))
qtree.insert((4, -7))
qtree.insert((-7, -8))

# Deletion tests
print("\nQNode Delete Status:")
print(qtree.delete((0, 0))) # Should fail
print(qtree.delete((-5, 7)))
print(qtree.delete((8, -6)))
print(qtree.delete((-3, -4)))

# Output to file
tree = qtree.tree_build()
tree.save2file("qtreeTest")

# Test the region searching
nodes = []
print("\nQNode search_region tests:")
print("\nFirst search_region:")
qtree.search_region(nodes, 2, 9, 4, -3, MAXLEFT, MAXRIGHT, MAXUP, MAXDOWN)
for node in nodes:
    print(node.point)
nodes.clear()
print("\nSecond search_region:")
qtree.search_region(nodes, -6, -2, 8, 3, MAXLEFT, MAXRIGHT, MAXUP, MAXDOWN)
for node in nodes:
    print(node.point)
nodes.clear()
print("\nThird search_region:")
qtree.search_region(nodes, -3, 8, 4, -7, MAXLEFT, MAXRIGHT, MAXUP, MAXDOWN)
for node in nodes:
    print(node.point)
nodes.clear()