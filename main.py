import matrices
#import tests

class UserPrompt:
    def __init__(self) -> None:
        self.edge_list = []


    def edge_list_input(self):
        # must be changed to accept different type of input (lines of pairs of ints)
        print(
            "Warning! This program accepts only integer values. Negative integers will be converted to their absolute "
            "value. The array cannot be empty.\nChoose natural key values. If you want to stop adding the edges press "
            "enter without typing any values. Note: the first key will always be assumed to be 0 and the last will be\n"
            "assumed to be the greatest number typed. Keys not used will still have their nodes created if they fall\n"
            "in range of 0 and max key, but they will not affect the usability of an algorithm.")
        while True:
            x = input(
                "Please enter your numbers as pairs, entering one pair at the time, one whitespace between each number: "
                "and one new line between each pair")
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
            
            if len(array) == 2:
                self.edge_list.append(array)
            else:
                print("Too many numbers in a row.")




    def user_loop(self):
        options_looper = self.edge_list_input
        while not options_looper:
            options_looper = self.edge_list_input

    
    # def file_loop(self):



    def main_loop(self) -> None:
        while True:
            s = input(
                "Choose one of the following options: [testing, user input, file input]. ").lower()
            if s == "user input":
                self.user_loop()
                s = input(
                    "If you want to exit the program, enter [exit]. Otherwise press Enter to try again. ")
                if s == "exit":
                    return

            elif s == "file input":
                self.file_loop()
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

            else:
                print("Please enter the correct option.")


if __name__ == '__main__':
    prompt = UserPrompt()
    prompt.main_loop()
