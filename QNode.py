
class QNode:

    def __init__(self, region, dim, point):
        self.region = region
        self.point = point
        self.children = []
        self.dim = dim

        # CHECK THIS
        self.num_children = 2**dim
        self.NULL = 0

        # Constants for dim = 2
        self.NW = 0
        self.NE = 1
        self.SW = 2
        self.SE = 3
        self.EQUAL = 4

        # Initialize a list with NULL children
        for i in range(0, self.num_children - 1):
            self.children.append(self.NULL)

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

    def insert(self, region, key):
        direction = self.compare(key)

        # Insert an element that is already present
        # We do not allow duplicates
        if direction == self.EQUAL:
            return self.NULL

        # Recursive case
        if self.children[direction] != self.NULL:
            return self.children[direction].insert(region, key)

        # Base case
        else:
            self.children[direction] = QNode(region, self.dim, key)





    def delete(self, key):
        pass

