
import treelib as tl

class QNode:

    def __init__(self, point):
        self.point = point
        self.children = []

        # Changes by dimension of datastructure.
        self.num_children = 4

        # Constants for dim = 2
        self.NW = 0
        self.NE = 1
        self.SW = 2
        self.SE = 3
        self.EQUAL = 4

        # Initialize a list with NULL children
        for i in range(0, self.num_children):
            self.children.append(None)

    """Tests if a singular point is within the passed region. Implemented for 2D data."""
    def test_point_region(self, left, right, up, down, point):
        if point[0] >= left and point[0] <= right and point[1] <= up and point[1] >= down:
            return True
        return False

    """Tests if a passed region overlaps a passed region. Implemented for 2D data."""
    def test_rect_region(self, tleft, tright, tup, tdown, left, right, up, down):
        if tleft <= right and tright >= left and tup >= down and tdown <= up:
            return True
        return False

    """Fills a passed list with nodes within the passed region. The bounds are inclusive.
        The search region is bounded by tleft, tright, tup, and tdown.
        left, right, up, and down is the region that could overlap the search region.
        For the first call, let left, right, up, down be set to the max and min values of the tree."""
    def search_region(self, nodes, tleft, tright, tup, tdown, left, right, up, down):

        # if this node lies in the region
        if self.test_point_region(tleft, tright, tup, tdown, self.point):

            nodes.append(self)

        # Recursively search the children's regions, if they overlap.
        if not (self.children[self.NW] is None) and self.test_rect_region(
                tleft, tright, tup, tdown, left, self.point[0], up, self.point[1]):
            self.children[self.NW].search_region(nodes, tleft, tright, tup, tdown, left, self.point[0], up,
                                                 self.point[1])

        if not (self.children[self.NE] is None) and self.test_rect_region(
                tleft, tright, tup, tdown, self.point[0], right, up, self.point[1]):
            self.children[self.NE].search_region(nodes, tleft, tright, tup, tdown, self.point[0], right, up,
                                                 self.point[1])

        if not (self.children[self.SW] is None) and self.test_rect_region(
                tleft, tright, tup, tdown, left, self.point[0], self.point[1], down):
            self.children[self.SW].search_region(nodes, tleft, tright, tup, tdown, left, self.point[0], self.point[1],
                                                 down)

        if not (self.children[self.SE] is None) and self.test_rect_region(
                tleft, tright, tup, tdown, self.point[0], right, self.point[1], down):
            self.children[self.SE].search_region(nodes, tleft, tright, tup, tdown, self.point[0], right, self.point[1],
                                                 down)

    """Returns what quadrant of the node the passed subtree lies in."""
    def compare(self, subpoint):
        if (subpoint[0] == self.point[0]) and (subpoint[1] == self.point[1]):
            return self.EQUAL
        elif self.point[0] < subpoint[0]:
            if self.point[1] < subpoint[1]:
                return self.NE
            else:
                return self.SE
        else:
            if self.point[1] < subpoint[1]:
                return self.NW
            else:
                return self.SW

    """Creates a node in the Qtree with the passed key. Returns success status."""
    def insert(self, point):
        direction = self.compare(point)

        # Insert an element that is already present
        # We do not allow duplicates
        if direction == self.EQUAL:
            return 1

        # Base case
        if self.children[direction] is None:
            self.children[direction] = QNode(point)
            return 0

        # Recursive case
        else:
            return self.children[direction].insert(point)

    """Returns true if the point passed is in the quad tree."""
    def contains(self, point):
        direction = self.compare(point)

        # The key is in the datastructure.
        if direction == self.EQUAL:
            return True

        # Base case
        if self.children[direction] is None:
            return False

        # Recursive case
        else:
            return self.children[direction].contains(point)

    """Relatively expensive. """
    def delete(self, point):
        pass

    """Helper function for the tree_build() function."""
    def tree_helper(self, parent, qtree):
        direction = parent.compare(self.point)

        # Test direction, add appropriate label, call method on children.
        if direction == self.NW:
            qtree.create_node("NW/" + str(self.point), self.point, parent.point)

            for node in self.children:
                if not (node is None):
                    node.tree_helper(self, qtree)

        elif direction == self.NE:
            qtree.create_node("NE/" + str(self.point), self.point, parent.point)

            for node in self.children:
                if not (node is None):
                    node.tree_helper(self, qtree)

        elif direction == self.SW:
            qtree.create_node("SW/" + str(self.point), self.point, parent.point)

            for node in self.children:
                if not (node is None):
                    node.tree_helper(self, qtree)

        elif direction == self.SE:
            qtree.create_node("SE/" + str(self.point), self.point, parent.point)

            for node in self.children:
                if not (node is None):
                    node.tree_helper(self, qtree)

        else:
            print("ERROR: equal comparison")

    """Returns a treelib tree of the node, used for illustration purposes."""
    def tree_build(self):
        qtree = tl.Tree()

        # Create root
        qtree.create_node(str(self.point), self.point)

        # Call the helper on all the children.
        for node in self.children:
            if not (node is None):
                node.tree_helper(self, qtree)

        return qtree
