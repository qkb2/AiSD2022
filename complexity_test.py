import time
from typing import Callable

import sorts_with_counters
import generator


def placebo_random_test(n):
    arr = generator.random_generator(n)
    start_time = time.perf_counter()
    sorted(arr)
    stop_time = time.perf_counter()
    return stop_time-start_time


def general_test(n, sortfun, genfun):
    arr = sortfun(n)
    start_time = time.perf_counter()
    genfun(arr)
    stop_time = time.perf_counter()
    return stop_time-start_time



def testing_suit_helper(n: int, amount: int, sortfun: Callable, genfun: Callable):
    comparisons = 0
    swaps = 0
    time = 0
    for _ in range(amount):
        arr = genfun(n)
        data = sortfun(arr)
        comparisons += data[1]
        swaps += data[2]
        time += data[3]
    comparisons /= amount
    swaps /= amount
    time /= amount
    return comparisons, swaps, time


def standard_testing_suit(array: list, sortfun: Callable):
    comparisons_n = []
    swaps_n = []
    times_n = []
    i = 0
    for genfun in [generator.random_generator, generator.increasing_generator, generator.decreasing_generator, generator.a_shaped_generator, generator.v_shaped_generator]:
        comparisons_n.append([])
        swaps_n.append([])
        times_n.append([])

        for n in array:
            c, sw, t = testing_suit_helper(n, 10, sortfun, genfun)
            comparisons_n[i].append(c)
            swaps_n[i].append(sw)
            times_n[i].append(t)

        i += 1
    return comparisons_n, swaps_n, times_n


def insert_testing():
    return standard_testing_suit(
        [10, 50, 100, 500, 750, 800, 900, 1000, 1100, 1250], sorts_with_counters.insertion_sort_wrapper)

def shell_testing():
    return standard_testing_suit(
        [10, 50, 100, 500, 750, 1000, 1250, 1500, 1750, 2000], sorts_with_counters.insertion_sort_wrapper)

def quick_testing():
    return standard_testing_suit(
        [10, 50, 100, 500, 1000, 1250, 1500, 1750, 2000, 2500], sorts_with_counters.quick_sort_wrapper)

def merge_testing():
    return standard_testing_suit(
        [10, 50, 100, 500, 1000, 5000, 10_000, 15_000, 20_000, 25_000], sorts_with_counters.merge_sort_wrapper)

def heap_testing():
    return standard_testing_suit(
        [10, 50, 100, 500, 1000, 5000, 10_000, 15_000, 20_000, 25_000], sorts_with_counters.heap_sort_wrapper)

# don't use the automatic testing - it lags too much.


def test_one():
    print("n' = 10n: ")
    for i in range(7):
        print(i, "   ", placebo_random_test(10**i))

    print("\nsame n:")
    avg = 0
    for i in range(10):
        t = placebo_random_test(10_000)
        avg += t
        print(t)
    print("average case: ", avg/10)

    return None




if __name__ == '__main__':
    #test_one()
    x = sorts_with_counters.insertion_sort_wrapper(generator.decreasing_generator(3000))
    print(x[1], x[2], x[3])