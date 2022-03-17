# main file which should execute a prompt for the users and/or the random tests

import sorts_with_counters


# TODO: automatic tests, user prompt wrappers

class UserPrompt:
    def __init__(self) -> None:
        self.sorting_opt = ""
        self.sorting_array = []

    def algo_options(self):
        opt = input(
            "Please choose the sorting algorithm by typing one of the following: [insert, shell, quick, merge, heap]: ")
        opt = opt.lower()

        if opt not in ["insert", "shell", "quick", "merge", "heap"]:
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

        try:
            array = list(map(int, array))
        except ValueError:
            print("The input seems to include non-numbers")
            return False

        self.sorting_array = list(map(abs, array))
        return True

    def main_loop(self):
        options_looper = self.algo_options()
        while not options_looper:
            options_looper = self.algo_options()
        options_looper = self.array_options()
        while not options_looper:
            options_looper = self.array_options()

        if self.sorting_opt == "insert":
            sorted_array, comparisons, swaps, time = sorts_with_counters.insertion_sort_wrapper(
                self.sorting_array)
            print("Sorted the array {} to {}".format(
                self.sorting_array, sorted_array))
            print("Comparisons made: {}. Swaps made: {}. Time taken: {}".format(
                comparisons, swaps, time))
            return None

        if self.sorting_opt == "merge":
            sorted_array, comparisons, merges, time = sorts_with_counters.merge_sort_wrapper(
                self.sorting_array)
            print("Sorted the array {} to {}".format(
                self.sorting_array, sorted_array))
            print("Comparisons made: {}. Merges made: {}. Time taken: {}".format(
                comparisons, merges, time))
            return None

        if self.sorting_opt == "heap":
            sorted_array, comparisons, swaps, time = sorts_with_counters.heap_sort_wrapper(
                self.sorting_array)
            print("Sorted the array {} to {}".format(
                self.sorting_array, sorted_array))
            print("Comparisons made: {}. Swaps made: {}. Time taken: {}".format(
                comparisons, swaps, time))
            return None

        if self.sorting_opt == "quick":
            sorted_array, comparisons, swaps, time, pivots = sorts_with_counters.quick_sort_wrapper(
                self.sorting_array)
            print("Sorted the array {} to {}".format(
                self.sorting_array, sorted_array))
            print("Comparisons made: {}. Swaps made: {}. Time taken: {}".format(
                comparisons, swaps, time))
            print("Pivots used: {}".format(pivots))
            return None

        if self.sorting_opt == "shell":
            sorted_array, comparisons, swaps, time, knuth = sorts_with_counters.shell_sort_wrapper(
                self.sorting_array)
            print("Sorted the array {} to {}".format(
                self.sorting_array, sorted_array))
            print("Comparisons made: {}. Swaps made: {}. Time taken: {}".format(
                comparisons, swaps, time))
            print("Knuth's sequence used: {}".format(knuth))
            return None

if __name__ == '__main__':
    prompt = UserPrompt()
    prompt.main_loop()

