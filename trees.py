import copy
from sorts import merge_sort


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


def traversal_wrapper(func):
    def wrapper(*args, **kwargs):
        sorted_nodes = []
        func(*args, sorted_nodes, **kwargs)

        return sorted_nodes

    return wrapper


class AvlTree:

    def __init__(self):
        self.nodes = []

    def generate(self, array: list):
        # sort the array with a given sort alg
        # choose median point
        # make median point the root and split the rest
        # proceed until len = 1

        if len(array) == 1:
            return array[0]

        # sorting array if not sorted
        sort_arr = array
        if sort_arr != sorted(array):
            sort_arr = merge_sort(array)[::-1]
        med = len(array) // 2

        # getting the median of the sorted array and making a node
        nd = Node(sort_arr[med])
        sort_arr[med] = None

        # getting the left and right nodes
        nd.left = self.generate(sort_arr[:med])
        nd.right = self.generate(sort_arr[med + 1 if len(array) > 2 else med:])

        self.nodes.append(nd)
        return nd.key

    def get_node(self, val: int):
        try:
            f_node = list(filter(lambda x: x.key == val, self.nodes))[0]
        except:
            f_node = None

        return f_node

    def find_node(self, val: int):
        try:
            f_node = list(
                filter(
                    lambda x: x.key == val or x.left == val or x.right == val,
                    self.nodes
                )
            )[0]
        except:
            f_node = None

        return f_node

    def traverse_pre_order(self, nd: Node, nd_arr: list):
        # root first, then left and then right

        if nd:
            # print the root
            nd_arr.append(nd.key)

            # find and print the left node if exists
            left_node = self.get_node(nd.left)
            if not left_node:
                if nd.left:
                    nd_arr.append(nd.left)

            self.traverse_pre_order(left_node, nd_arr)

            # find and print the right node if exists
            right_node = self.get_node(nd.right)
            if not right_node:
                if nd.right:
                    nd_arr.append(nd.right)

            self.traverse_pre_order(right_node, nd_arr)

    def traverse_in_order(self, nd: Node, nd_arr: list):
        # left first, then root and then right

        if nd:
            # find and print the left node if exists
            left_node = self.get_node(nd.left)
            if not left_node:
                if nd.left:
                    nd_arr.append(nd.left)

            self.traverse_in_order(left_node, nd_arr)

            # print the root
            nd_arr.append(nd.key)

            # find and print the right node if exists
            right_node = self.get_node(nd.right)
            if not right_node:
                if nd.right:
                    nd_arr.append(nd.right)

            self.traverse_in_order(right_node, nd_arr)

    def traverse_post_order(self, nd: Node, nd_arr: list):
        # left first, then right and then root

        if nd:
            # find and print the left node if exists
            left_node = self.get_node(nd.left)
            if not left_node:
                if nd.left:
                    nd_arr.append(nd.left)

            self.traverse_post_order(left_node, nd_arr)

            # find and print the right node if exists
            right_node = self.get_node(nd.right)
            if not right_node:
                if nd.right:
                    nd_arr.append(nd.right)

            self.traverse_post_order(right_node, nd_arr)

            # print the root
            nd_arr.append(nd.key)

    def find_min(self, nd: Node):
        if nd:
            print(nd.key, "-> ", end="")
            if not nd.left:
                mn = nd.key
                return mn
            left_node = self.get_node(nd.left)
            if not left_node:
                if nd.left:
                    mn = nd.left
                    return mn

            return self.find_min(left_node)

    def find_max(self, nd: Node):
        if nd:
            print(nd.key, "-> ", end="")
            if not nd.right:
                mn = nd.key
                return mn
            right_node = self.get_node(nd.right)
            if not right_node:
                if nd.right:
                    mn = nd.right
                    return mn

            return self.find_max(right_node)

    def remove_leaf_or_ochn(self, val: int):
        # locate the value
        f_node = self.get_node(val)
        if not f_node:
            f_node = self.find_node(val)
            if not f_node:
                return

        # if value is leaf, just remove
        if val == f_node.left:
            f_node.left = None
        if val == f_node.right:
            f_node.right = None

        # elif value has one child, remove value, make child root
        # and update tree
        if val == f_node.key:
            if f_node.left and not f_node.right:
                n_key = copy.deepcopy(f_node.key)
                f_node.key = f_node.left
                f_node.left = None
                p_node = self.find_node(n_key)

                if p_node.left == n_key:
                    p_node.left = f_node.key
                if p_node.right == n_key:
                    p_node.right = f_node.key

            elif f_node.right and not f_node.left:
                n_key = copy.deepcopy(f_node.key)
                f_node.key = f_node.right
                f_node.right = None
                p_node = self.find_node(n_key)

                if p_node.left == n_key:
                    p_node.left = f_node.key
                if p_node.right == n_key:
                    p_node.right = f_node.key

        # elif value has two children, remove value, make neighbour (in value) a root
        if val == f_node.key:
            self.remove_root(f_node)

    def remove_root(self, nd: Node):
        # sort nodes in-order
        # get one of the neighbours and set as root
        # remove the neighbour from its previous position

        srt_nd = traversal_wrapper(avl.traverse_in_order)(nd)
        neigh = None

        for i in range(len(srt_nd)):
            if srt_nd[i] == nd.key:
                if i + 1 < len(srt_nd):
                    neigh = srt_nd[i + 1]
                else:
                    neigh = srt_nd[i - 1]

        self.remove_leaf_or_ochn(neigh)
        nd.key = neigh

    def print_tree(self):
        for k in self.nodes:
            print(k.key, k.left, k.right)


class TreeHandler:

    def generate_tree(self, typ, array):
        None


if __name__ == '__main__':
    avl = AvlTree()
    root = avl.generate([1, 3, 2, 8, 4, 7, 5, 13])
    avl.print_tree()

    root_node = avl.get_node(root)
    user_node = avl.get_node(8)

    # traverse pre the whole tree
    print("----- pre-order whole")
    print(traversal_wrapper(avl.traverse_pre_order)(root_node))
    # traverse pre the subtree
    print("----- pre-order sub")
    print(traversal_wrapper(avl.traverse_pre_order)(user_node))
    # traverse in the whole tree
    print("----- in-order whole")
    print(traversal_wrapper(avl.traverse_in_order)(root_node))
    # traverse post the whole tree
    print("----- post-order whole")
    print(traversal_wrapper(avl.traverse_post_order)(root_node))

    # find min
    print("----- min")
    print(avl.find_min(root_node))
    # find max
    print("----- max")
    print(avl.find_max(root_node))

    # remove leaf
    print("----- removing leaf")
    avl.remove_leaf_or_ochn(13)
    avl.print_tree()
    # remove one child
    print("----- removing one child node")
    avl.remove_leaf_or_ochn(2)
    avl.print_tree()
    # remove root
    print("----- removing root")
    avl.remove_leaf_or_ochn(5)
    avl.print_tree()


# TODO:
# tree construction: AVL with binary search, random BST
# the following procedures are to be implemented for both tree types:
# finding the max and min values in the tree and printing the root->min/max value node path
# deleting an element of the tree by providing the amount of elements to be deleted and their keys
# printing all the elements in in-order
# printing all the elements in pre-order
# deleting the whole tree in post-order (printing the elements before they are deleted)
# printing a subtree with a root being a key chosen by the user in pre-order
# balancing the tree by either rotation (DSW) or by root deletion
# input: n-element random sequence provided by the user, n-element descending random sequence provided by the generator
# output: sorting time plus printing all the procedures
# time should be measured on: 1) structure creation 2) searching for the min. value 3) in-order printing
# for BST time should also be measured on BST balancing
# testing: one point on a plot is an avg of 10 samples
# plot should have at least 10 values of n, SD should also be provided
