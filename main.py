
class QNode:

    def __init__(self, key, dim):
        self.key = key
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

        # Initialize a list with NULL children
        for i in range(0, self.num_children - 1):
            self.children.append(self.NULL)

