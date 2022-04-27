import matrices
import tests
from os.path import isfile

class UserPrompt:
    def __init__(self) -> None:
        self.edge_list = []
        self.V = 0
        self.E = 0


    def edge_list_input(self):
        self.edge_list = []
        # must be changed to accept different type of input (lines of pairs of ints)
        print(
            "Warning! This program accepts only integer values. Negative integers will be converted to their absolute "
            "value. The array cannot be empty.\nChoose natural key values. If you want to stop adding the edges press "
            "enter without typing any values. Note: the first key will always be assumed to be 1 and the last will be\n"
            "assumed to be the greatest number typed. Keys not used will still have their nodes created if they fall\n"
            "in range of 1 and max key, but they will not affect the usability of an algorithm.")
        while True:
            x = input(
                "Please enter your numbers as pairs, entering one pair at the time, one whitespace between each number: "
                "and one new line between each pair\n")
            if x == '':
                if len(self.edge_list) != 0:
                    return True
                return False

            array = x.split()
            try:
                array = list(map(int, array))
            except ValueError:
                print("The input seems to include non-numbers")
                continue
            
            if array[0] == 0 or array[1] == 0:
                print("The key cannot be 0")
                continue

            if len(array) == 2:
                self.edge_list.append(array)
            else:
                print("Too many numbers in a row.")

    def edge_list_from_file(self):
        self.edge_list = []
        # must be changed to accept different type of input (lines of pairs of ints)
        print(
            "Warning! This program accepts only integer values. Negative integers will be converted to their absolute "
            "If the file contains any discrepencies, zeroes etc. there will be an error.")
        faddr = ''
        while True:
            faddr = input("Please enter a correct path to a file.")
            if isfile(faddr) and faddr.endswith(".txt"):
                break
            else:
                print("Path incorrect.")
            
        with open(faddr, "r") as fread:
            x = fread.readline()
            if x == '':
                return False
            array = x.split()
            try:
                array = list(map(int, array))
            except ValueError:
                print("Values corrupted. Choose a different file.")
                return False
                
            if array[0] == 0:
                print("The graph cannot be empty. Choose a different file.")
                return False

            self.V = array[0]
            self.E = array[1]
            c = 0
         
            while c < array[1]:
                c += 1
                x = fread.readline()
                if x == '':
                    if len(self.edge_list) != 0:
                        return True
                    return False

                array = x.split()
                try:
                    array = list(map(int, array))
                except ValueError:
                    continue
                
                if array[0] == 0 or array[1] == 0:
                    continue

                if len(array) == 2:
                    self.edge_list.append(array)

    def user_loop(self, s: str):
        if s == 'file loop':
            options_looper = self.edge_list_from_file()
            while not options_looper:
                options_looper = self.edge_list_from_file()
        else:
            options_looper = self.edge_list_input()
            while not options_looper:
                options_looper = self.edge_list_input()           


    def display_results(self):
        mat = matrices.TheSaintMatrix()
        mat.create_matrix_wrapper(self.edge_list)
        mat.build_the_saint_matrix()
        print("Adjacency matrix:")
        print(mat)
        print("Matrix of a graph following the prof. Szachniuk's convention:")
        print(mat.get_str())
        print("Sorting the graph with both algorithms.")
        arr1 = mat.kahn_top_sort()
        arr2 = mat.dfs_top_sort()
        if len(arr1) != len(arr2):
            print("An error occured. Exiting...")
            return
        print("Topologically sorted arrays gotten by:\nKahn's sort: {}\nDFS-based sort: {}".format(arr1, arr2))


    def main_loop(self) -> None:
        while True:
            s = input(
                "Choose one of the following options: [testing, user input, file input]. ").lower()
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
                tests.testing_suit()
                return
            
            elif s == "file input":
                self.edge_list_from_file()
                self.display_results()
                s = input(
                    "If you want to exit the program, enter [exit]. Otherwise press Enter to try again. ")
                if s == "exit":
                    return

            else:
                print("Please enter the correct option.")


if __name__ == '__main__':
    prompt = UserPrompt()
    prompt.main_loop()
