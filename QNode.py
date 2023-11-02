
class QNode:

    def __init__(self, region, dim, point):
        self.region = region # used to represent colour
        self.point = point
        self.children = []
        self.dim = dim

        # CHECK THIS
        self.num_children = 2**dim

        # Constants for dim = 2
        self.NW = 0
        self.NE = 1
        self.SW = 2
        self.SE = 3
        self.EQUAL = 4

        # Initialize a list with NULL children
        for i in range(0, self.num_children - 1):
            self.children.append(None)

    """Tests if a singular point is within the passed region. Implemented for 2D data."""
    def test_point_region(self, left, right, up, down, point):
        if point[0] >= left and point[0] <= right and point[1] <= up and point[1] >= down:
            return True
        return False

    """Tests if a passed region is within a passed region. Implemented for 2D data."""
    def test_rect_region(self, tleft, tright, tup, tdown, left, right, up, down):
        if tleft <= right and tright >= left and tup >= down and tdown <= up:
            return True
        return False

    """Fills a passed list with nodes within the passed region."""
    def search_region(self, nodes, tleft, tright, tup, tdown, left, right, up, down):

        # if this node lies in the region
        if self.test_point_region(left, right, up, down, self.point):
            nodes.append(self)

        # Recursively search the children
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

    """Creates a node in the Qtree with the passed key and the passed region"""
    def insert(self, region, point):
        direction = self.compare(point)

        # Insert an element that is already present
        # We do not allow duplicates
        if direction == self.EQUAL:
            return 1

        # Base case
        if self.children[direction] is None:
            self.children[direction] = QNode(region, self.dim, point)
            return 0

        # Recursive case
        else:
            return self.children[direction].insert(region, point)

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









    def delete(self, key):
        pass

