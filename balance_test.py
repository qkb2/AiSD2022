from tests import test_wrapper
import trees
tree_hand = trees.TreeHandler()
tree, t = tree_hand.generate_tree(False, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
t = tree_hand.get_balancing_rmr_time(tree)
print(tree)
print(t)
#print(test_wrapper(False, 100, 0))