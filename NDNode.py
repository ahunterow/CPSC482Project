
import treelib as tl

"""Experimental. An attempt at an "N-dimensional quad tree," this class represents a Node within that tree,
as well as the tree itself."""
class NDNode:

    def __init__(self, point):
        self.point = point
        self.children = []
        self.dim = len(self.point)

        # CHECK THIS
        self.num_children = 2 ** self.dim

        # Equality constant
        self.LESS = 0
        self.EQUAL = -1
        self.GREAT = 1
        self.ROUNDING_DIRECTION = self.GREAT # This determines behaviour of point equality in certain dimensions.

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

    """Helper method of compare, returns a value, LESS indicating val is less than the sub_val, 
        GREAT if val is greater than sub_val, and EQUAL if both arguments are equal."""
    def compare_val(self, val, sub_val):
        if val < sub_val:
            return self.LESS
        elif val > sub_val:
            return self.GREAT
        else:
            return self.EQUAL

    """Returns what subspace of the node the passed subtree lies in."""
    def compare(self, subpoint):

        direction = ""

        # Equality check
        is_equal = True

        # Make a string of comparisons across all dimensions.
        for index, sub_val in enumerate(subpoint):
            comparison = self.compare_val(self.point[index], sub_val)

            # Keep track of point equality
            if comparison != self.EQUAL:
                is_equal = False

            # If there is equality in a dimension, alter it to the ROUNDING_DIRECTION
            else:
                comparison = self.ROUNDING_DIRECTION

            direction = direction + str(comparison)

        # These comparisons are a list of bits. Taking these comparisons and treating them as a binary number
        # and converting them to decimal number allows mapping to a subspace within the list of children.
        subspace = int(direction, 2)

        return subspace


    """Creates a node in the Qtree with the passed key. Returns success status."""
    def insert(self, point):
        direction = self.compare(point)

        # Insert an element that is already present
        # We do not allow duplicates
        if direction == self.EQUAL:
            return 1

        # Base case
        if self.children[direction] is None:
            self.children[direction] = NDNode(point)
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

    """Returns the node found at the passed point, if it is present."""
    def search(self, point):
        direction = self.compare(point)

        # The key is in the datastructure.
        if direction == self.EQUAL:
            return self

        # Base case
        if self.children[direction] is None:
            return None

        # Recursive case
        else:
            return self.children[direction].contains(point)

    """Helper method for the delete_helper() function."""
    def reinsert(self, root):
        root.insert(self.point)

        # Reinsert every stranded node back into the tree
        for node in self.children:
            if not (node is None):
                node.reinsert(root)

    """Helper method for the delete() function."""
    def delete_helper(self, point, parent, root):
        direction = self.compare(point)

        # The point is located
        if direction == self.EQUAL:

            # Delete the subtree from the parent
            reference_num = parent.compare(self.point)
            parent.children[reference_num] = None

            # Reinsert every stranded node back into the tree
            for node in self.children:
                if not (node is None):
                    node.reinsert(root)

            return 0

        # Base case, the node to delete is not in the tree
        if self.children[direction] is None:
            return 1

        # Recursive case, proceed to find the node.
        else:
            return self.children[direction].delete_helper(point, self, root)

    """Relatively expensive. Deletes a passed point from the quad tree, returns success status.
    Due to the reference to the tree being a QNode, there must always be at least one node in the tree.
    Thus, it is enforced that one cannot delete the root."""
    def delete(self, point):
        direction = self.compare(point)

        # Deleting the root.
        if direction == self.EQUAL:
            return 1

        # Base case
        if self.children[direction] is None:
            return 1

        # Recursive case
        else:
            return self.children[direction].delete_helper(point, self, self)

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
