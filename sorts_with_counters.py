# I/O requirements (REVERSE ORDER):
# sorting time, amount of operations (comparisons and swaps, for merge sort only comparisons)
# for user-inserted input also:
# original and sorted array, pivots in every iteration for quicksort, amount of merges in merge sort, increment value for shell sort


import time
import sys


sys.setrecursionlimit(1_000_000)



class Counter:
    def __init__(self) -> None:
        self.counter = 0

    def add(self, i: int) -> None:
        self.counter += i


# DONE: comparisons and merges counter
def merge(left_array: list, right_array: list, array: list, c: Counter) -> None:
    # function merges both arrays together
    # next element to be added to the array is chosen from the greatest elements from both L and R arrays.
    # val. l and r increment every time their greater element is merged (so that l and r always point towards the next
    # variable element that wasn't added to the array
    l = r = k = 0
    while l < len(left_array) and r < len(right_array):
        c.add(3)  # two for the while loop above and one for the if below
        if left_array[l] > right_array[r]:
            array[k] = left_array[l]
            l += 1
        else:
            array[k] = right_array[r]
            r += 1
        k += 1

    # checks if there was something left in either array
    while l < len(left_array):
        c.add(1)
        array[k] = left_array[l]
        l += 1
        k += 1

    while r < len(right_array):
        c.add(1)
        array[k] = right_array[r]
        r += 1
        k += 1

    return None


def merge_sort(array: list, c: Counter, merges: Counter) -> tuple[list, Counter, Counter]:
    c.add(1)
    if len(array) > 1:
        midway = len(array)//2
        left_array = array[:midway]
        right_array = array[midway:]
        # recursion - the array is split in the middle (mid-point)
        merge_sort(left_array, c, merges)
        merge_sort(right_array, c, merges)
        merges.add(1)
        merge(left_array, right_array, array, c)

    return array, c, merges


def merge_sort_wrapper(array: list) -> tuple[list, int, int, float]:
    c = Counter()
    merges = Counter()
    start_time = time.perf_counter()
    merge_sort(array, c, merges)
    stop_time = time.perf_counter()
    cc = c.counter
    mm = merges.counter
    return array, cc, mm, stop_time-start_time


# DONE: comparisons and swaps counter
def heapify(array: list, parent_idx: int, heap_size: int, c: Counter, swaps: Counter) -> None:
    # this recursive procedure produces a min-heap structure by first comparing both of the children to their parent and
    # arranging them in a proper heap-order. If the structure changed the heapify procedure is called once more to "fix"
    # the sub-heap affected by the change
    left_child_idx = 2 * parent_idx + 1
    right_child_idx = 2 * parent_idx + 2
    largest_idx = parent_idx
    c.add(1)
    if left_child_idx < heap_size:
        c.add(1)
        if array[largest_idx] > array[left_child_idx]:
            largest_idx = left_child_idx

    c.add(1)
    if right_child_idx < heap_size:
        c.add(1)
        if array[largest_idx] > array[right_child_idx]:
            largest_idx = right_child_idx

    c.add(1)
    if largest_idx != parent_idx:
        array[largest_idx], array[parent_idx] = array[parent_idx], array[largest_idx]
        swaps.add(1)
        heapify(array, largest_idx, heap_size, c, swaps)

    return None


def build_heap(array: list, c: Counter, swaps: Counter) -> list:
    # the len(array)//2-1 is the index of the last parent
    for i in range(len(array)//2-1, -1, -1):
        c.add(1)
        heapify(array, i, len(array), c, swaps)

    return array


def heap_sort(array: list, c: Counter, swaps: Counter) -> list:
    build_heap(array, c, swaps)
    for i in range(len(array)-1, 0, -1):
        c.add(1)
        array[i], array[0] = array[0], array[i]
        swaps.add(1)
        heapify(array, 0, i, c, swaps)

    return array


def heap_sort_wrapper(array: list) -> tuple[list, int, int, float]:
    c = Counter()
    swaps = Counter()
    start_time = time.perf_counter()
    heap_sort(array, c, swaps)
    stop_time = time.perf_counter()
    cc = c.counter
    sw = swaps.counter
    return array, cc, sw, stop_time-start_time


# DONE: comparisons and swaps counter
def insertion_sort(array: list, c: Counter, swaps: Counter) -> list:
    for i in range(1, len(array)):
        c.add(1)
        key = array[i]
        j = i-1
        while j >= 0 and array[j] < key:
            c.add(2)
            array[j+1] = array[j]
            swaps.add(1)
            j -= 1

        array[j+1] = key

    return array


def insertion_sort_wrapper(array: list) -> tuple[list, int, int, float]:
    c = Counter()
    swaps = Counter()
    start_time = time.perf_counter()
    insertion_sort(array, c, swaps)
    stop_time = time.perf_counter()
    cc = c.counter
    sw = swaps.counter
    return array, cc, sw, stop_time-start_time


# DONE: comparisons and swaps counter, increments
def helper_insert(array: list, step: int, c: Counter, swaps: Counter) -> list:
    for i in range(1, len(array)-step+1, step):
        c.add(1)
        key = array[i]
        j = i - step
        while j >= 0 and array[j] < key:
            c.add(2)
            array[j + step] = array[j]
            swaps.add(1)
            j -= step

        array[j + step] = key

    return array


def shell_sort(array: list, c: Counter, swaps: Counter, knuth: list) -> list:
    step = 0
    while step < len(array)//3:
        c.add(1)
        step = 3*step+1

    while step > 0:
        c.add(1)
        knuth.append(step)
        helper_insert(array, step, c, swaps)
        step = (step-1)//3

    return array


def shell_sort_wrapper(array: list) -> tuple[list, int, int, float, list]:
    c = Counter()
    swaps = Counter()
    knuth = []
    start_time = time.perf_counter()
    shell_sort(array, c, swaps, knuth)
    stop_time = time.perf_counter()
    cc = c.counter
    sw = swaps.counter
    return array, cc, sw, stop_time-start_time, knuth


# DONE: comparisons and swaps counter, pivots
def partition(array: list, low: int, high: int, c: Counter, swaps: Counter) -> int:
    pivot = array[high]  # pivot chosen as the last element of a sequence
    i = low-1
    for j in range(low, high):
        c.add(2)
        if array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            swaps.add(1)

    array[i+1], array[high] = array[high], array[i+1]
    swaps.add(1)
    return i+1


def quick_sort_recursive(array: list, low: int, high: int, c: Counter, swaps: Counter, pivots: list) -> list:
    c.add(1)
    if len(array) == 1:
        return array

    c.add(1)
    if low < high:
        pivot = partition(array, low, high, c, swaps)
        pivots.append(pivot)
        quick_sort_recursive(array, low, pivot - 1, c, swaps, pivots)
        quick_sort_recursive(array, pivot + 1, high, c, swaps, pivots)

    return array


def quick_sort(array: list, c: Counter, swaps: Counter, pivots: list):
    return quick_sort_recursive(array, 0, len(array)-1, c, swaps, pivots)


def quick_sort_wrapper(array: list) -> tuple[list, int, int, float, list]:
    c = Counter()
    swaps = Counter()
    pivots = []
    start_time = time.perf_counter()
    quick_sort(array, c, swaps, pivots)
    stop_time = time.perf_counter()
    cc = c.counter
    sw = swaps.counter
    return array, cc, sw, stop_time-start_time, pivots
