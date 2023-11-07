# Driver for testing the quad tree.

import treelib as tl

from QNode import *

MAXLEFT = -10
MAXRIGHT = 10
MAXUP = 10
MAXDOWN = -10


# root
qtree = QNode((0, 0))

# test data
qtree.insert((-5,7))
qtree.insert((-3,-4))
qtree.insert((-4,4))
qtree.insert((4,3))
qtree.insert((8,-6))
qtree.insert((-9,6))
qtree.insert((3,-2))
qtree.insert((6,7))
qtree.insert((8,2))
qtree.insert((4,-7))
qtree.insert((-7,-8))

tree = qtree.tree_build()
tree.save2file("qtreeTest")

# print(qtree.contains((-4,4)))

# nodes = []
# qtree.search_region(nodes, 2, 9, 4, -3, MAXLEFT, MAXRIGHT, MAXUP, MAXDOWN)
# qtree.search_region(nodes, -6, -2, 8, 3, MAXLEFT, MAXRIGHT, MAXUP, MAXDOWN)
# qtree.search_region(nodes, -3, 8, 4, -7, MAXLEFT, MAXRIGHT, MAXUP, MAXDOWN)
# for node in nodes:
#     print(node.point)

