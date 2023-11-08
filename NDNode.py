
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

    """Tests if a singular point is within the passed bounds. Bounds should be a list of tuples.
        Each tuple represents the bounds for one dimension in the ordering (lower, upper). Thus,
        it follows that their must be as many tuples as dimensions in the point. Returns 1 if the point 
        is present in the bounds, 0 if the point is not in the bounds, and -1 if an error occured."""
    def test_point_region(self, point, bounds):

        # Checking that the right number of bounds has been passed
        if len(point) != len(bounds):
            print("ERROR: incorrect number of bounds for data.")
            return -1

        within_region = True

        # Check each set of bounds
        for index, bound in enumerate(bounds):
            # Make sure we have valid bounds.
            if not (bound[0] < bound[1]):
                return -1

            # if point not in bounds
            if not (point[index] >= bound[0]) and (point[index] <= bound[1]):
                within_region = False
                break

        if within_region:
            return 1
        else:
            return 0

    """Tests if a region overlaps with the passed bounds. Bounds should be a list of tuples, 
        as should the region defined by test_bounds.
        Each tuple represents the bounds for one dimension in the ordering (lower, upper). Thus,
        it follows that their must be as many tuples as dimensions in the point. Returns 1 if the overlaps
        the bounds, 0 if the does not overlap the bounds, and -1 if an error occured."""
    def test_region_region(self, test_bounds, bounds):

        # Checking that the right number of bounds has been passed
        if len(test_bounds) != len(bounds):
            print("ERROR: incorrect number of bounds for data.")
            return -1

        overlaps_region = True

        # Check all dimensions for overlap
        for index, bound in enumerate(bounds):
            # Make sure we have valid bounds.
            if not (bound[0] < bound[1]):
                return -1

            # if the region does not overlap.
            if not (test_bounds[index][0] <= bound[1]) and (test_bounds[index][1] >= bound[0]):
                overlaps_region = False
                break

        if overlaps_region:
            return 1
        else:
            return 0

    """TODO Fills a passed list with nodes within the passed region. The passed region is test_bounds, and it
        is a list of tuples of bounds, of the form (lower, upper), one tuple for each
        dimension of the data. The search bounds are inclusive.
        For the first call, bounds should be a list of tuples of bounds, of the form (lower, upper), one tuple for each
        dimension of the data, and these bounds should encompass the whole tree structure."""
    def search_region(self, nodes, test_bounds, bounds):

        # if this node lies in the region
        if self.test_point_region(self.point, test_bounds):

            nodes.append(self)

        # Use the direction to restrict the bounds on the search space.

        for direction, child in enumerate(self.children):

            if not (child is None):
                # Get the comparisons that are made to get into this direction
                # This means taking the direction and mapping it to a string of bits
                comparisons = bin(direction)
                comparisons = comparisons[slice(2, len(comparisons))] # Trim off the "0b" at the start.
                comparisons = comparisons.zfill(self.dim) # Add leading 0s on to the left as needed.

                # Restrict bounds.
                sub_bounds = bounds.copy()

                for index, bound in enumerate(sub_bounds):

                    # If the node's value is greater, then restrict the upper bound.
                    # Otherwise, restrict the lower bound.
                    # Done for every set of bounds
                    if int(comparisons[index]) == self.GREAT:
                        sub_bounds[index] = (bound[0], self.point[index])
                    else:
                        sub_bounds[index] = (self.point[index], bound[1])

                # if the tested bounds fall in the subspace defined by sub_bounds.
                if self.test_region_region(test_bounds, sub_bounds):
                    # Recursive case.
                    child.search_region(nodes, test_bounds, sub_bounds)


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

        if is_equal:
            return self.EQUAL
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

    """TODO Helper method for the delete_helper() function."""
    def reinsert(self, root):
        root.insert(self.point)

        # Reinsert every stranded node back into the tree
        for node in self.children:
            if not (node is None):
                node.reinsert(root)

    """TODO Helper method for the delete() function."""
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

    """TODO Relatively expensive. Deletes a passed point from the quad tree, returns success status.
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

    """TODO Helper function for the tree_build() function."""
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

    """TODO Returns a treelib tree of the node, used for illustration purposes."""
    def tree_build(self):
        qtree = tl.Tree()

        # Create root
        qtree.create_node(str(self.point), self.point)

        # Call the helper on all the children.
        for node in self.children:
            if not (node is None):
                node.tree_helper(self, qtree)

        return qtree
