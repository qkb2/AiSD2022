from sorts import merge_sort

class node:

    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class avl_tree:

    def __init__(self):
        self.nodes = []

    def generate(self, array: list):
        # sort the array with a given sort alg
        # choose median point
        # make median point the root and split the rest
        # procede until len = 1

        if len(array) == 1:
            return array[0]

        # sorting array if not sorted
        sort_arr = array
        if sort_arr != sorted(array):
            sort_arr = merge_sort(array)[::-1]
        med = len(array) // 2

        # getting the median of the sorted array and making a node
        nd = node(sort_arr[med])
        sort_arr[med] = None

        # getting the left and right nodes
        nd.left = self.generate(sort_arr[:med])
        nd.right = self.generate(sort_arr[med + 1 if len(array) > 2 else med:])

        self.nodes.append(nd)
        return nd.key

    def traverse_pre_order(self, nd: node):
        # root first, then left and then right

        if nd:
            # print the root
            print(nd.key)

            # find and print the left node if exists
            try:
                left_node = list(
                    filter(lambda x: x.key == nd.left, self.nodes)
                )[0]
            except:
                left_node = None
                if nd.left:
                    print(nd.left)

            self.traverse_pre_order(left_node)

            # find and print the right node if exists
            try:
                right_node = list(
                    filter(lambda x: x.key == nd.right, self.nodes)
                )[0]
            except:
                right_node = None
                if nd.right:
                    print(nd.right)

            self.traverse_pre_order(right_node)

    def print_tree(self):
        for k in self.nodes:
            print(k.key, k.left, k.right)


class tree_handler:

    def generate_tree(self, typ, array):
        None


if __name__ == '__main__':
    avl = avl_tree()
    root = avl.generate([1, 3, 2, 8, 4, 7, 5, 13])
    avl.print_tree()
    root_node = list(filter(lambda x: x.key == root, avl.nodes))[0]
    avl.traverse_pre_order(root_node)

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
# testing: one point on a plot is an avg of 10 samples, plot should have at least 10 values of n, SD should also be provided
