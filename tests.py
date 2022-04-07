# input: n-element descending random sequence provided by the generator, output: time
# time should be measured on: 1) structure creation 2) searching for the min. value 3) in-order printing
# for BST time should also be measured on 4) BST balancing
# testing: one point on a plot is an avg of 10 samples
# plot should have at least 10 values of n, SD should also be provided

import csv

import trees
from old_utilities import decreasing_generator as gen


def test_wrapper(is_avl: bool, n: int, i):
    print("\n{} test".format(i))
    tree_hand = trees.TreeHandler()
    tree, gen_time = tree_hand.generate_tree(is_avl, gen(n, 10*n))
    search_time = tree_hand.get_min_time(tree)
    trav_time = tree_hand.get_in_order_time(tree)
    if is_avl:
        bal_time = 0
    else:
        bal_time = tree_hand.get_balancing_rmr_time(tree)
    return gen_time, search_time, trav_time, bal_time



def testing_handler(is_avl: bool, array: list, sample: int):
    with open('data_is_avl_{}.csv'.format(is_avl), 'w+', newline='') as csvf:
        csvwriter = csv.writer(csvf, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for n in array:
            #csvf.write("{} generate search traverse balance\n".format(n))
            for i in range(sample):
                time_array = test_wrapper(is_avl, n, i)
                time_array = list(map(str, time_array))
                csvf.write(str(n)+" ")
                csvwriter.writerow(time_array)
    csvf.close()


def testing_suit() -> None:
    arr  =[i for i in range(50, 550, 50)]
    testing_handler(True, arr, 10)
    testing_handler(False, arr, 10)


if __name__ == '__main__':
    testing_suit()