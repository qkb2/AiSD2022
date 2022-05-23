from tests import test_wrapper
from old_project_trees.old_utilities import decreasing_generator as gen
import trees
tree_hand = trees.TreeHandler()
l = gen(100, 1000)
print(l)
tree, t = tree_hand.generate_tree(False, l)
t = tree_hand.get_balancing_rmr_time(tree)
print(tree)
print(t)
#print(test_wrapper(False, 100, 0))