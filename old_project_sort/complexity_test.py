import time
import csv
from typing import Callable

import sorts_with_counters
import generator


def placebo_random_test(n):
    arr = generator.random_generator(n)
    start_time = time.perf_counter()
    sorted(arr)
    stop_time = time.perf_counter()
    return stop_time-start_time


def time_test(n, sortfun, genfun):
    arr = sortfun(n)
    start_time = time.perf_counter()
    genfun(arr)
    stop_time = time.perf_counter()
    return stop_time-start_time


def testing_for_users(n: int, i: int, algo: str, gen: str):
    if algo == "insert":
        sortfun = sorts_with_counters.insertion_sort_wrapper

    elif algo == "merge":
        sortfun = sorts_with_counters.merge_sort_wrapper

    elif algo == "heap":
        sortfun = sorts_with_counters.heap_sort_wrapper

    elif algo == "quick":
        sortfun = sorts_with_counters.quick_sort_wrapper

    elif algo == "shell":
        sortfun = sorts_with_counters.shell_sort_wrapper


    if gen == "random":
        genfun = generator.random_generator

    elif gen == "increasing":
        genfun = generator.increasing_generator

    elif gen == "decreasing":
        genfun = generator.decreasing_generator

    elif gen == "a shaped":
        genfun = generator.a_shaped_generator

    elif gen == "v shaped":
        genfun = generator.v_shaped_generator

    testing_helper(n, i, sortfun, genfun)
    



def testing_helper(n: int, iter: int, sortfun: Callable, genfun: Callable):

    experiment_data = []
    avg_comp = 0
    avg_swaps = 0
    avg_time = 0

    for i in range(iter):
        experiment_data.append([])
        arr = genfun(n)
        data = sortfun(arr)
        avg_comp += data[1]
        avg_swaps += data[2]
        avg_time += data[3]
        experiment_data[i].append(str(data[1]))
        experiment_data[i].append(str(data[2]))
        experiment_data[i].append(str(data[3]))

    avg_comp /= iter
    avg_swaps /= iter
    avg_time /= iter

    with open('data.csv', 'a', newline='') as csvf:
        csvf.write('{} {} {} {}'.format(sortfun.__name__, genfun.__name__, n, iter))
        csvf.write('\n')
        csvwriter = csv.writer(csvf, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['comparisons', 'swaps', 'time'])
        for i in range(iter):
            csvwriter.writerow(experiment_data[i])
        
        csvwriter.writerow([str(avg_comp), str(avg_swaps), str(avg_time)])
        csvf.write('\n')
        csvf.close()

    return None


def testing_suit():
    for sortfun in [
        sorts_with_counters.insertion_sort_wrapper, sorts_with_counters.shell_sort_wrapper, sorts_with_counters.quick_sort_wrapper, sorts_with_counters.merge_sort_wrapper, sorts_with_counters.heap_sort_wrapper]:
        for genfun in [
            generator.random_generator, generator.increasing_generator, generator.decreasing_generator, generator.a_shaped_generator, generator.v_shaped_generator]:
            for n in [x*250 for x in range(1, 13)]:
                testing_helper(n, 10, sortfun, genfun)



# # don't use the automatic testing - it lags too much.


# def test_one():
#     print("n' = 10n: ")
#     for i in range(7):
#         print(i, "   ", placebo_random_test(10**i))

#     print("\nsame n:")
#     avg = 0
#     for i in range(10):
#         t = placebo_random_test(10_000)
#         avg += t
#         print(t)
#     print("average case: ", avg/10)

#     return None




if __name__ == '__main__':
    # x = sorts_with_counters.quick_sort_wrapper(generator.increasing_generator(1000))
    # print(x[1], x[2], x[3])
    testing_suit()