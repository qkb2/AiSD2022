import trees


class UserPrompt:
    def __init__(self) -> None:
        self.is_avl = True
        self.sorting_array = []
        self.tree_hand = trees.TreeHandler()

    def tree_options(self):
        opt = input("Please choose the tree type: [BST, AVL]: ")
        opt = opt.lower()

        if opt not in ["bst", "avl"]:
            print("This name is not recognised")
            return False

        if opt == "avl":
            self.is_avl = True
        else:
            self.is_avl = False
        return True

    def array_options(self):
        # array_options can be used generally as a troll handler - for example if the user was to enter a key that is
        # actually not a number the array_options can be called to handle it until they provide the proper numbers
        print(
            "Warning! This program accepts only integer values. Negative integers will be converted to their absolute "
            "value. The array cannot be empty.")
        array = input(
            "Please enter your numbers as a one line, one whitespace between each of them: ").split()

        if len(array) == 0:
            print("The input should not be empty")
            return False

        # if len(array) > 10:
        #     print("The amount of numbers should not be greater than 10.")
        #     return False

        try:
            array = list(map(int, array))
        except ValueError:
            print("The input seems to include non-numbers")
            return False

        self.sorting_array = list(map(abs, array))
        return True

    def tree_interactions(self) -> str:
        opt = input("What should be done with the tree provided?:\n[find min, find max, print in order, print pre order, "
                    "del post order, remove elements, print subtree, balance bst]\nshorter: [MIN, MAX, IN, PRE, DEL, REM, "
                    "SUB, BAL].\nTo exit type [exit] instead: ")
        opt = opt.lower()

        if opt not in ["find min", "find max", "print in order", "print pre order", "delete post order", "remove elements",
                       "print subtree", "balance bst", "min", "max", "in", "pre", "del", "rem", "sub", "bal", "exit"]:
            print("This name is not recognised")
            return "fail"
        return opt

    def tree_options(self, tree: trees.AvlTree) -> None:
        while True:
            opt = self.tree_interactions()
            # tree handler returns float val. of time for all its methods besides the tree generator
            if opt == "fail":
                continue
            elif opt == "exit":
                return
            elif opt == "find min" or opt == "min":
                t = self.tree_hand.get_min_time(tree)
                print("Time taken: {}".format(t))
            elif opt == "find max" or opt == "max":
                x = tree.find_max()
                print(x)
            elif opt == "print in order" or opt == "in":
                t = self.tree_hand.get_in_order_time(tree)
                print("Time taken: {}".format(t))
            elif opt == "print pre order" or opt == "pre":
                print(trees.traversal_wrapper(
                    tree.traverse_pre_order)(tree.get_root()))
            elif opt == "delete post order" or opt == "del":
                t = 0  # TODO: apply the method for post-order deletion
                print(
                    "The tree has been removed in {} seconds. Exiting to the previous menu.".format(t))
                return
            elif opt == "remove elements" or opt == "rem":
                key = int(input())
                tree.remove_any_node(key)
                # TODO: checker for numbers, actually get some use out of node remover
                # should probably take int args, not nodes
            elif opt == "print subtree" or opt == "sub":
                s = input("Enter a correct key: ")
                key = 0
                while True:
                    try:
                        key = abs(int(s))
                        break
                    except ValueError:
                        print("The input seems not to be an integer.")
                        continue
                if key not in self.sorting_array:
                    print("There is no such node in this tree.")
                print(trees.traversal_wrapper(
                    tree.traverse_pre_order)(tree.get_node(key)))
            elif opt == "balance bst" or opt == "bal":
                if self.is_avl:
                    print("AVL tree is already balanced.")
                else:
                    t = self.tree_hand.get_balancing_time(tree)
                    print("Balanced the BST in {} seconds.".format(t))

    def user_loop(self):
        options_looper = self.tree_options()
        while not options_looper:
            options_looper = self.tree_options()
        options_looper = self.array_options()
        while not options_looper:
            options_looper = self.array_options()

        tree, t = self.tree_hand.generate_tree(
            self.is_avl, self.sorting_array)  # True means AVL
        print("AVL Tree was created in {} seconds.".format(t))
        self.tree_options(tree)

    # finding the max and min values in the tree and printing the root->min/max value node path
    # deleting an element of the tree by providing the amount of elements to be deleted and their keys
    # printing all the elements in in-order
    # printing all the elements in pre-order
    # deleting the whole tree in post-order (printing the elements before they are deleted)
    # printing a subtree with a root being a key chosen by the user in pre-order
    # balancing the tree by either rotation (DSW) or by root deletion
    # input: n-element random sequence provided by the user
    # output: sorting time plus printing all the procedures
    # time should be measured on: 1) structure creation 2) searching for the min. value 3) in-order printing

    def main_loop(self):
        while True:
            s = input(
                "Choose one of the following options: [testing, user input]. ").lower()
            if s == "user input":
                self.user_loop()
                s = input(
                    "If you want to exit the program, enter [exit]. Otherwise press Enter to try again. ")
                if s == "exit":
                    return

            elif s == "testing":
                print(
                    "Warning! Auto-testing takes a long time to complete and its completion is dependent on the "
                    "user's computer specs. The data will be generated in the data.csv file.")
                print(
                    "Now wait for the data collection to complete. After that, the program will automatically shut "
                    "down.")
                # tree_test.testing_suit()
                return

            else:
                print("Please enter the correct option.")


if __name__ == '__main__':
    prompt = UserPrompt()
    prompt.main_loop()
