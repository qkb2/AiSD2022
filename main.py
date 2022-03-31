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
        print(
            "Warning! This program accepts only integer values. Negative integers will be converted to their absolute value. The array cannot be empty.")
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

        if self.sorting_opt == "bst":
            # see: TODO on trees
            print("test user BST")
            return

        else:
            # see: TODO on trees
            print("test user AVL")
            return


    def main_loop(self):
        while True:
            s = input("Choose one of the following options: [testing, user input]. ").lower()
            if s == "user input":
                self.user_loop()
                s = input("If you want to exit the program, enter one of the following: [q, exit, quit]. Otherwise press Enter to try again. ")
                if s == "q" or s == "exit" or s == "quit":
                    return
                
            elif s == "testing":
                print(
                    "Warning! Auto-testing takes a long time to complete and its completion is dependent on the user's computer specs. The data will be generated in the data.csv file.")
                print("Now wait for the data collection to complete. After that, the program will automatically shut down.")
                # tree_test.testing_suit()
                return
            
            else:
                print("Please enter the correct option.")

if __name__ == '__main__':
    prompt = UserPrompt()
    prompt.main_loop()