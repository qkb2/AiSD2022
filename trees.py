import copy
import time
from old_utilities import merge_sort  # this one sorts normally (1,2...)


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


# util functions
def traversal_wrapper(func):
    def wrapper(*args, **kwargs):
        sorted_nodes = []
        func(*args, sorted_nodes, **kwargs)

        return sorted_nodes

    return wrapper


def calc_hei_wrapper(func):
    def wrapper(*args, **kwargs):
        height = []
        func(*args, height, **kwargs)

        return sum(height)

    return wrapper


class AvlTree:

    def __init__(self):
        self.nodes = []
        self.root = None

    def generate_avl(self, array: list):
        # sort the array with a given sort alg
        # choose median point
        # make median point the root and split the rest
        # proceed until len = 1

        if len(array) == 1:
            return array[0]

        # sorting array if not sorted
        sort_arr = array
        # if sort_arr != sorted(array):
        # sort_arr = merge_sort(array)
        med = len(array) // 2

        # getting the median of the sorted array and making a node
        nd = Node(sort_arr[med])
        sort_arr[med] = None

        # getting the left and right nodes
        nd.left = self.generate_avl(sort_arr[:med])
        nd.right = self.generate_avl(sort_arr[med + 1 if len(array) > 2 else med:])

        self.nodes.append(nd)

        self.root = nd
        return nd.key

    def get_root(self):
        return self.root

    def calc_height(self, nd: Node, height: list):

        if nd:
            height.append(1)

            left_node = self.get_node(nd.left)
            if not left_node:
                right_node = self.get_node(nd.right)
                if not right_node:
                    if nd.left or nd.right:
                        height.append(1)
                else:
                    self.calc_height(right_node, height)
            else:
                self.calc_height(left_node, height)

    def calc_balance(self, nd: Node):
        # if leaf then balance 0
        # if one child then balance 1
        # if two children then balance 0
        # if subtree than calc height

        left_node = self.get_node(nd.left)
        right_node = self.get_node(nd.right)

        l_h = 0
        r_h = 0
        if not left_node:
            if nd.left:
                l_h += 1
        else:
            l_h += calc_hei_wrapper(self.calc_height)(left_node)

        if not right_node:
            if nd.right:
                r_h += 1
        else:
            r_h += calc_hei_wrapper(self.calc_height)(right_node)

        return abs(l_h - r_h)

    def is_balanced(self):
        # check the factor of balance for each root-node
        # (diff between the height of the left subtree and the h of the right sbt)
        # if some factor > 1 then not balanced

        for nd in self.nodes:
            nd_balance = self.calc_balance(nd)
            if nd_balance > 1:
                return False

        return True

    def balance(self):
        # sort the nodes in in-order order
        # feed the sorted array to generate_avl function

        srt_nd = traversal_wrapper(self.traverse_in_order)(self.get_root())
        self.nodes = []
        self.generate_avl(srt_nd)

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

    def find_min(self, nd: Node = None):

        if not nd:
            nd = self.root

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

    def find_max(self, nd: Node = None):

        if not nd:
            nd = self.root

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

            # if value is leaf that was a root
            elif not f_node.right and not f_node.left:
                n_key = copy.deepcopy(f_node.key)
                self.nodes.remove(f_node)
                p_node = self.find_node(n_key)

                if p_node.left == n_key:
                    p_node.left = None
                if p_node.right == n_key:
                    p_node.right = None

        # elif value has two children, remove value, make neighbour (in value) a root
        if val == f_node.key:
            self.remove_root(f_node)

    def remove_root(self, nd: Node):
        # sort nodes in-order
        # get one of the neighbours and set as root
        # remove the neighbour from its previous position

        srt_nd = traversal_wrapper(self.traverse_in_order)(nd)
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

    def remove_any_node(self, key: int):
        if key == self.root.key:
            self.remove_root(self.get_root())
        else:
            self.remove_leaf_or_ochn(key)
            # TODO: something with remove root and remove leaf having different arg types


class BstRandom(AvlTree):

    def __init__(self):
        super().__init__()

    def generate_random(self, array: list):
        # iterate through array elements
        # build the tree one by one

        # make first element root
        # then put next elements in tree by looping
        # all the nodes, and placing it in left or right
        # if it doesn't exist in the tree yet

        root_nd = None
        for i in range(len(array)):
            if len(self.nodes) == 0:
                nd = Node(array[i])
                self.nodes.append(nd)
                root_nd = nd
            else:
                for n in self.nodes:
                    if not self.find_node(array[i]):
                        if array[i] < n.key:
                            if not n.left:
                                n.left = array[i]
                            else:
                                if array[i] < n.left:
                                    if not self.get_node(n.left):
                                        nd = Node(n.left)
                                        nd.left = array[i]
                                        self.nodes.append(nd)
                                elif array[i] > n.left:
                                    if not self.get_node(n.left):
                                        nd = Node(n.left)
                                        nd.right = array[i]
                                        self.nodes.append(nd)
                        elif array[i] > n.key:
                            if not n.right:
                                n.right = array[i]
                            else:
                                if array[i] < n.right:
                                    if not self.get_node(n.right):
                                        nd = Node(n.right)
                                        nd.left = array[i]
                                        self.nodes.append(nd)
                                elif array[i] > n.right:
                                    if not self.get_node(n.right):
                                        nd = Node(n.right)
                                        nd.right = array[i]
                                        self.nodes.append(nd)

        self.root = root_nd
        return root_nd.key


class TreeHandler:

    def generate_tree(self, avl: bool, array: list):

        if avl:
            tree = AvlTree()
            sort_arr = array
            if sort_arr != sorted(array):
                sort_arr = merge_sort(array)
            start_time = time.perf_counter()
            tree.generate_avl(sort_arr)
            stop_time = time.perf_counter()
        else:
            tree = BstRandom()
            start_time = time.perf_counter()
            tree.generate_random(array)
            stop_time = time.perf_counter()

        return tree, stop_time - start_time

    def get_min_time(self, tree):

        start_time = time.perf_counter()
        print(tree.find_min())
        stop_time = time.perf_counter()

        return stop_time - start_time

    def get_in_order_time(self, tree):

        start_time = time.perf_counter()
        print(traversal_wrapper(tree.traverse_in_order)(tree.get_root()))
        stop_time = time.perf_counter()

        return stop_time - start_time

    def get_balancing_time(self, tree):

        start_time = time.perf_counter()
        tree.balance()
        stop_time = time.perf_counter()

        return stop_time - start_time


if __name__ == '__main__':
    tree_hand = TreeHandler()

    avl_g, avl_t = tree_hand.generate_tree(True, [1, 3, 2, 8, 4, 7, 5, 13])
    bst_g, bst_t = tree_hand.generate_tree(False, [1, 3, 2, 8, 4, 7, 5, 13])

    print("----- avl tree, time: ", avl_t)
    avl_g.print_tree()

    print("----- bst tree, time: ", bst_t)
    bst_g.print_tree()

    print("")
    avl_m_t = tree_hand.get_min_time(avl_g)
    print("----- avl find min time: ", avl_m_t)
    bst_m_t = tree_hand.get_min_time(bst_g)
    print("----- bst find min time: ", bst_m_t)

    print("")
    avl_i_t = tree_hand.get_in_order_time(avl_g)
    print("----- avl in-order time: ", avl_i_t)
    bst_i_t = tree_hand.get_in_order_time(bst_g)
    print("----- bst in-order time: ", bst_i_t)

    print("")
    avl_b_t = tree_hand.get_balancing_time(avl_g)
    bst_b_t = tree_hand.get_balancing_time(bst_g)
    print("----- avl balancing time: ", avl_b_t)
    print("----- bst balancing time: ", bst_b_t)

    # avl = AvlTree()
    # root = avl.generate_avl([1, 3, 2, 8, 4, 7, 5, 13])
    # avl.print_tree()
    # print("----- root is: ", root)

    # user_node = avl.get_node(8)

    # # check if balanced
    # print("----- is balanced")
    # print(avl.is_balanced())

    # # traverse pre the whole tree
    # print("----- pre-order whole")
    # print(traversal_wrapper(avl.traverse_pre_order)(avl.get_root()))
    # # traverse pre the subtree
    # print("----- pre-order sub")
    # print(traversal_wrapper(avl.traverse_pre_order)(user_node))
    # # traverse in the whole tree
    # print("----- in-order whole")
    # print(traversal_wrapper(avl.traverse_in_order)(avl.get_root()))
    # # traverse post the whole tree
    # print("----- post-order whole")
    # print(traversal_wrapper(avl.traverse_post_order)(avl.get_root()))

    # # find min
    # print("----- min")
    # print(avl.find_min())
    # # find max
    # print("----- max")
    # print(avl.find_max())

    # # remove leaf
    # print("----- removing leaf")
    # avl.remove_leaf_or_ochn(13)
    # avl.remove_leaf_or_ochn(7)
    # avl.remove_leaf_or_ochn(8)
    # avl.print_tree()
    # # remove one child
    # # print("----- removing one child node")
    # # avl.remove_leaf_or_ochn(2)
    # # avl.print_tree()
    # # remove root
    # # print("----- removing root")
    # # avl.remove_leaf_or_ochn(5)
    # # avl.print_tree()

    # # check if balanced
    # print("----- is balanced")
    # print(avl.is_balanced())
    # # balance tree
    # print("----- balancing tree")
    # avl.balance()
    # avl.print_tree()
    # # check if balanced
    # print("----- is balanced")
    # print(avl.is_balanced())

    # # generating random bst
    # print("----- random bst")
    # bst = BstRandom()
    # bst_root = bst.generate_random([1, 3, 2, 8, 4, 7, 5, 13])
    # bst.print_tree()
    # print("----- root is: ", bst_root)

    # # traverse pre the whole tree
    # print("----- pre-order whole")
    # print(traversal_wrapper(bst.traverse_pre_order)(bst.get_root()))
    # # traverse pre the subtree
    # print("----- pre-order sub")
    # print(traversal_wrapper(bst.traverse_pre_order)(bst.get_node(8)))
    # # traverse in the whole tree
    # print("----- in-order whole")
    # print(traversal_wrapper(bst.traverse_in_order)(bst.get_root()))
    # # traverse post the whole tree
    # print("----- post-order whole")
    # print(traversal_wrapper(bst.traverse_post_order)(bst.get_root()))

    # # balancing random bst
    # print("----- random bst balanced")
    # print(bst.is_balanced())
    # bst.balance()
    # bst.print_tree()
    # print(bst.is_balanced())

    # # find min
    # print("----- min")
    # print(bst.find_min())
    # # find max
    # print("----- max")
    # print(bst.find_max())

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
