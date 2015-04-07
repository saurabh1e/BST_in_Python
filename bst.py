# coding=utf-8
__author__ = 'saurabh'


class Node(object):
    """
    :return
    """
    def __init__(self, info):  # constructor of class

        self.info = info  # information for node
        self.left = None  # left node
        self.right = None  # right node
        self.level = None  # level of node
        self.parent = None

    def __str__(self):
        return str(self.info)


class SearchTree(object):
    """

    :return:
    """

    def __init__(self):  # constructor of class

        self.root = None

    def create(self, val):  # create binary search tree nodes and assign levels
        """
        :param val:
        :return:
        """

        if self.root is None:
            self.root = Node(val)
            self.root.level = 0
            self.root.parent = None
        else:
            current = self.root
            count = 0
            while 1:
                count += 1
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        current.left.parent = current
                        current.left.level = count
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        current.right.parent = current
                        current.right.level = count
                        break

    def bft(self):  # Breadth-First Traversal
        """

        :return:
        """
        queue = [self.root]
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_level < current_node.level:
                current_level = current_node.level
                print " "
            print current_node.info,

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)
        return 0

    def in_order(self, node):
        """

        :param node:
        :return:
        """

        if node is not None:
            self.in_order(node.left)
            print node.info, "",
            self.in_order(node.right)
        return 0

    def pre_order(self, node):
        """

        :param node:
        :return:
        """

        if node is not None:
            print node.info, "",
            self.pre_order(node.left)
            self.pre_order(node.right)
        return 0

    def post_order(self, node):
        """

        :param node:
        :return:
        """

        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print node.info, "",
        return 0

    def search(self, value):
        """
        :param value:
        :return:
        """
        self.root.level = 0
        current_node = self.root
        while 1:
            if current_node.info == value:
                print "found element", value, "at level ->", current_node.level
                return current_node

            elif current_node.info > value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    print "element->", value, "not found"
                    return -1

            elif current_node.info < value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    print "element->", value, "not found"
                    return -1

        return current_node

    def del_element(self, value):
        """
        :param value:
        :return:
        """
        current_node = self.root
        while 1:
            if current_node.info == value:
                if current_node.left and current_node.right:
                    left_node = current_node.left
                    right_node = current_node.right
                    if right_node.left:
                        while right_node.left is not None:
                            right_node = right_node.left

                        print right_node
                        left_node.parent = right_node
                        parent_node = right_node.parent
                        parent_node.left = None
                        right_node.parent = current_node.parent
                        right_node.left = left_node
                        right_node.right = current_node.right
                        current_node.right.parent = right_node
                        print current_node, right_node, left_node
                        if current_node == self.root:
                            self.root = right_node
                        print "Element->", value, "Deleted successfully"
                        return 0

                    else:
                        if current_node == self.root:
                            self.root = right_node
                        right_node.parent = current_node.parent
                        right_node.left = left_node
                        left_node.parent = right_node

                        current_node.parent = None
                        current_node.left = None
                        current_node.right = None
                        print "Element->", value, "Deleted successfully"
                        return 0

                if current_node.left and not current_node.right:
                    left_node = current_node.left
                    if current_node.parent.left is current_node:
                        current_node.parent.left = left_node
                    else:
                        current_node.parent.right = left_node
                    left_node.parent = current_node.parent
                    if current_node == self.root:
                        self.root = left_node
                    current_node.parent = None
                    current_node.left = None
                    current_node.right = None
                    if current_node.parent.left is current_node:
                        current_node.parent.left = left_node
                    else:
                        current_node.parent.right = left_node
                    print "Element->", value, "Deleted successfully"
                    return 0

                if current_node.right and not current_node.left:
                    right_node = current_node.right
                    if current_node == self.root:
                        self.root = right_node
                    if current_node.parent.left is current_node:
                        current_node.parent.left = right_node
                    else:
                        current_node.parent.right = right_node
                    right_node.parent = current_node.parent
                    current_node.parent = None
                    current_node.left = None
                    current_node.right = None
                    print "Element->", value, "Deleted successfully"
                    return 0

                if not current_node.right and not current_node.left:

                    if current_node.parent.left is current_node:
                        current_node.parent.left = None
                    else:
                        current_node.parent.right = None
                    current_node.parent = None
                    current_node.left = None
                    current_node.right = None
                    print "Element->", value, "Deleted successfully"
                    return 0

            elif current_node.info > value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    print "element->", value, "not found"
                    return -1

            elif current_node.info < value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    print "element->", value, "not found"
                    return -1

        else:
            print "element->", value, "not found"

    def level_reassign(self):
        """

        :return:
        """
        queue = [self.root]
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_level < current_node.level:
                current_level = current_node.level

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)


if __name__ == "__main__":

    print "Running Test Case 1 with values [8, 3, 1, 6, 4, 7, 10, 14, 13, 9]"
    tree = SearchTree()
    arr = [8, 3, 1, 6, 4, 7, 10, 14, 13, 9]
    for i in arr:
        tree.create(i)
    print '\nBreadth-First Traversal'
    tree.bft()
    print '\nIn order Traversal'
    tree.in_order(tree.root)
    print '\nPre order Traversal'
    tree.pre_order(tree.root)
    print '\nPost order Traversal'
    tree.post_order(tree.root)
    print '\nSearch element 6'
    tree.search(6)
    print '\nDelete element 8'
    tree.del_element(8)
    tree.level_reassign()
    print '\nNew BST is '
    tree.bft()
    print '\nDelete element 10'
    tree.del_element(9)
    tree.level_reassign()
    print '\nNew BST is '
    tree.bft()

    print "Running Test Case 2 with values [10, 15, 25, 3, 6, 8, 3, 4, 9, 11, 19, 24, 1, 2]"
    tree2 = SearchTree()
    arr2 = [10, 15, 25, 3, 6, 8, 4, 9, 11, 19, 24, 1, 2]
    for i in arr2:
        tree2.create(i)
    print '\nBreadth-First Traversal'
    tree2.bft()
    print '\nIn order Traversal'
    tree2.in_order(tree.root)
    print '\nPre order Traversal'
    tree2.pre_order(tree.root)
    print '\nPost order Traversal'
    tree2.post_order(tree.root)
    print '\nSearch element 11'
    tree2.search(11)
    print '\nDelete element 11'
    tree2.del_element(11)
    tree2.level_reassign()
    print '\nNew BST is '
    tree2.bft()
    print '\nDelete element 15'
    tree2.del_element(15)
    tree2.level_reassign()
    print '\nNew BST is '
    tree2.bft()