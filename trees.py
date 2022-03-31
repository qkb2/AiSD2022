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


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.data)
