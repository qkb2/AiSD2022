
from os.path import isfile


class UserPrompt:
    def __init__(self) -> None:
        self.array = []
        self.b = 0
        self.n = 0

    # TODO: add the ability for user to add the b and n
    def list_input(self):
        self.array = []
        # must be changed to accept different type of input (lines of pairs of ints)
        print(
            "Warning! This program accepts only integer values. Negative integers will be converted to their absolute "
            "value. The array cannot be empty.\nChoose natural values. If you want to stop adding the elements press "
            "enter without typing any values. Note: the indexes will be assumed to be from 0 to n-1, each element having\n"
            "its own index determined by order it was enter in. First pair entered should be the number of elements\n"
            "and the knapsack capacity b. If more than n elements are typed in, the program will automatically change the\n"
            "value of n to reflect that.")
        while True:
            x = input(
                "Please enter your numbers as pairs, entering one pair at the time, one whitespace between each number: "
                "and one new line between each pair\n")
            if x == '':
                if len(self.array) != 0:
                    self.n = len(self.array)
                    return True
                return False

            harr = x.split()
            try:
                harr = list(map(int, harr))
            except ValueError:
                print("The input seems to include non-numbers")
                continue

            if len(harr) == 2:
                self.array.append(harr)
            else:
                print("Too many numbers in a row.")

    def list_from_file(self):
        self.array = []
        # must be changed to accept different type of input (lines of pairs of ints)
        print(
            "Warning! This program accepts only integer values. Negative integers will be converted to their absolute "
            "values. If the file contains any discrepencies etc. there will be an error raised.")
        faddr = ''
        while True:
            faddr = input("Please enter a correct path to a file: ")
            if isfile(faddr) and faddr.endswith(".txt"):
                break
            else:
                print("Path incorrect.")

        with open(faddr, "r") as fread:
            x = fread.readline()
            if x == '':
                return False
            harr = x.split()
            try:
                harr = list(map(int, harr))
            except ValueError:
                print("Values corrupted. Choose a different file.")
                return False

            if harr[0] == 0:
                print("The list cannot be empty. Choose a different file.")
                return False

            self.n = harr[0]
            self.b = harr[1]
            c = 0

            while c < self.n:
                # print(c)
                c += 1
                x = fread.readline()
                if x == '':
                    if len(self.array) != 0:
                        self.n = len(self.array)
                        return True
                    return False

                harr = x.split()
                try:
                    harr = list(map(int, harr))
                except ValueError:
                    continue

                if len(harr) == 2:
                    self.array.append(harr)

    def user_loop(self, s: str):
        if s == 'file loop':
            options_looper = self.list_from_file()
            while not options_looper:
                options_looper = self.list_from_file()
        else:
            options_looper = self.list_input()
            while not options_looper:
                options_looper = self.list_input()

    def display_results(self):
        adj_mat = graphs.UndirAdjMatrix()
        adj_list = graphs.DirAdjList()
        adj_mat.create_matrix_wrapper(self.edge_list)
        adj_list.create_list_wrapper(self.edge_list)
        print("Undirected adjacency matrix:")
        print(adj_mat)
        print("Directed adjacency list:")
        print(adj_list)
        print("Searching for paths...")

        arr_ham_am = adj_mat.hamilton_wrapper()
        arr_eu_am = adj_mat.euler_wrapper()
        test_am = adj_mat.euler_decision()
        arr_ham_al = adj_list.hamilton_wrapper()
        arr_eu_al = adj_list.euler_wrapper()
        test_al = adj_list.euler_decision()

        print("Results:")
        if len(arr_ham_am) == 0:
            print("No hamiltonian path for undirected graph.")
        else:
            print("Hamiltonian path for undirected graph: {}".format(arr_ham_am))

        if len(arr_ham_am) == 0:
            print("No hamiltonian path for directed graph.")
        else:
            print("Hamiltonian path for directed graph: {}".format(arr_ham_al))

        if len(arr_eu_am) == 0 and not test_am:
            print("No eulerian path for undirected graph.")
        elif len(arr_eu_am) != 0 and test_am:
            print("Eulerian path for undirected graph: {}".format(arr_eu_am))
        else:
            print("An error ocurred (Euler - undirected).")

        if len(arr_eu_al) == 0 and not test_al:
            print("No eulerian path for directed graph.")
        elif len(arr_eu_al) != 0 and test_al:
            print("Eulerian path for directed graph: {}".format(arr_eu_al))
        else:
            print("An error ocurred (Euler - directed).")

    def main_loop(self) -> None:
        while True:
            s = input(
                "Choose one of the following options: [testing, user input, file input, exit]. ").lower()
            if s == "user input":
                self.user_loop(s)
                self.display_results()
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
                # tests.testing_suit()
                return

            elif s == "file input":
                self.list_from_file()
                self.display_results()
                s = input(
                    "If you want to exit the program, enter [exit]. Otherwise press Enter to try again. ")
                if s == "exit":
                    return

            elif s == "exit":
                return

            else:
                print("Please enter the correct option.")


if __name__ == '__main__':
    prompt = UserPrompt()
    prompt.main_loop()
