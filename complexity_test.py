import time

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

def general_test_with_counters(n: int, sortfun: function, genfun: function):
    arr = sortfun(n)
    data = genfun(arr)
    return data[1], data[2], data[3]


def standard_testing_suit(n: int, amount: int, sortfun: function, genfun: function):
    comparisons, swaps, time = 0
    for _ in range(amount):
        c, sw, t = general_test_with_counters(n, sortfun, genfun)
        comparisons += c
        swaps += sw
        time += t
    comparisons /= amount
    swaps /= amount
    time /= amount
    return comparisons, swaps, time


# def all_at_once():
#     testing_array = []
#     for n in testing_array:
#         standard_testing_suit(n, 10, )


if __name__ == '__main__':
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
