# Driver for testing the quad tree.

import treelib as tl

qtree = tl.Tree()
qtree.create_node("A", "a")
qtree.create_node("B", "b", parent="a")
qtree.create_node("C", "c", parent="a")
qtree.create_node("D", "d", parent="a")
qtree.create_node("E", "e", parent="a")
qtree.create_node("F", "f", parent="b")

qtree.save2file("qtreeTest")
#qtree.show()