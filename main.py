# Driver for testing the quad tree.

import treelib as tl

from QNode import *
from NDNode import *

# Constants for search_region's initial call.
MAXLEFT = -10
MAXRIGHT = 10
MAXUP = 10
MAXDOWN = -10

# root
qtree = NDNode((0, 0))

# Testing functions for binary mapping
# test = bin(4)
# test = test[slice(2, len(test))]
# test = test.zfill(8)
# print(int(test, 2))

# Test data for a quad tree
qtree.insert((-5,7))
# qtree.insert((-3,-4))
# qtree.insert((-4,4))
# qtree.insert((4,3))
# qtree.insert((8,-6))
# qtree.insert((-9,6))
# qtree.insert((3,-2))
# qtree.insert((6,7))
# qtree.insert((8,2))
# qtree.insert((4,-7))
# qtree.insert((-7,-8))

# tree = qtree.tree_build()
# tree.save2file("qtreeTest")

# print(qtree.delete((4, 3)))
# print(qtree.delete((-5, 7)))
# print(qtree.delete((8, -6)))
# print(qtree.delete((-3, -4)))
#
tree = qtree.tree_build()
tree.save2file("qtreeTest")

# print(qtree.contains((-4,4)))

# nodes = []
# qtree.search_region(nodes, 2, 9, 4, -3, MAXLEFT, MAXRIGHT, MAXUP, MAXDOWN)
# qtree.search_region(nodes, -6, -2, 8, 3, MAXLEFT, MAXRIGHT, MAXUP, MAXDOWN)
# qtree.search_region(nodes, -3, 8, 4, -7, MAXLEFT, MAXRIGHT, MAXUP, MAXDOWN)
# for node in nodes:
#     print(node.point)

