import trees


def tree_interactions() -> str:
    opt = input("What should be done with the tree provided?:\n[print in order, print pre order, delete post order, "
                "delete elements, print subtree, balance bst]\nshorter: [IN, PRE, DELPOST, DEL, SUB, BAL].\nTo exit "
                "type [exit] instead: ")
    opt = opt.lower()

    if opt not in ["print in order", "print pre order", "delete post order", "delete elements", "print subtree",
                   "balance bst", "in", "pre", "delpost", "del", "sub", "bal", "exit"]:
        print("This name is not recognised")
        return "fail"
    return opt


class UserPrompt:
    def __init__(self) -> None:
        self.sorting_opt = ""
        self.sorting_array = []

    def tree_options(self):
        opt = input("Please choose the tree type: [BST, AVL]: ")
        opt = opt.lower()

        if opt not in ["bst", "avl"]:
            print("This name is not recognised")
            return False

        self.sorting_opt = opt
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

    def user_loop(self):
        options_looper = self.tree_options()
        while not options_looper:
            options_looper = self.tree_options()
        options_looper = self.array_options()
        while not options_looper:
            options_looper = self.array_options()

        if self.sorting_opt == "avl":
            # see: TODO on trees
            while True:
                opt = tree_interactions()
                if opt == "fail":
                    continue
                elif opt == "exit":
                    break
                elif opt == "print in order" or opt == "in":
                    None
                elif opt == "print pre order" or opt == "pre":
                    None
                elif opt == "delete post order" or opt == "delpost":
                    print("The tree has been removed. Exiting to the previous menu.")
                    break
                elif opt == "delete elements" or opt == "del":
                    None
                elif opt == "print subtree" or opt == "sub":
                    None
                elif opt == "balance bst" or opt == "bal":
                    print("AVL tree is already balanced.")

        else:
            # see: TODO on trees
            print("test user BST")

            return

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

    def avl_loop(self):
        return

    def bst_loop(self):
        return

    def main_loop(self):
        while True:
            s = input("Choose one of the following options: [testing, user input]. ").lower()
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
