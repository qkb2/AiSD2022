# I/O requirements:
# sorting time, amount of operations (comparisons and swaps, for merge sort only comparisons)
# for user-inserted input also:
# original and sorted array, pivots in every iteration for quicksort, amount of merges in merge sort, increment value for shell sort


# DONE 1: merge sort
def merge(left_array, right_array, array):
    # function merges both arrays together
    # next element to be added to the array is chosen from the smallest elements from both L and R arrays.
    # val. l and r increment every time their smallest element is merged (so that l and r always point towards the next
    # variable element that wasn't added to the array
    l = r = k = 0
    while l < len(left_array) and r < len(right_array):
        if left_array[l] < right_array[r]:
            array[k] = left_array[l]
            l += 1
        else:
            array[k] = right_array[r]
            r += 1
        k += 1

    # checks if there was something left in either array
    while l < len(left_array):
        array[k] = left_array[l]
        l += 1
        k += 1

    while r < len(right_array):
        array[k] = right_array[r]
        r += 1
        k += 1

    return None


def merge_sort(array):
    if len(array) > 1:
        midway = len(array)//2
        left_array = array[:midway]
        right_array = array[midway:]
        # recursion - the array is split in the middle (mid-point)
        merge_sort(left_array)
        merge_sort(right_array)
        merge(left_array, right_array, array)

    return array


# DONE: heap sort
def heapify(array, parent_idx, heap_size):
    # this recursive procedure produces a max-heap structure by first comparing both of the children to their parent and
    # arranging them in a proper heap-order. If the structure changed the heapify procedure is called once more to "fix"
    # the sub-heap affected by the change
    left_child_idx = 2 * parent_idx + 1
    right_child_idx = 2 * parent_idx + 2
    largest_idx = parent_idx
    if left_child_idx < heap_size:
        if array[largest_idx] < array[left_child_idx]:
            largest_idx = left_child_idx

    if right_child_idx < heap_size:
        if array[largest_idx] < array[right_child_idx]:
            largest_idx = right_child_idx

    if largest_idx != parent_idx:
        array[largest_idx], array[parent_idx] = array[parent_idx], array[largest_idx]
        heapify(array, largest_idx, heap_size)

    return None


def build_heap(array):
    # the len(array)//2-1 is the index of the last parent
    for i in range(len(array)//2-1, -1, -1):
        heapify(array, i, len(array))

    return array


def heap_sort(array):
    build_heap(array)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)

    return array


# DONE: insertion sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

    return array


# DONE: shell-sort w/ knuth increments
def helper_insert(array, step):
    for i in range(1, len(array)-step+1, step):
        key = array[i]
        j = i - step
        while j >= 0 and array[j] > key:
            array[j + step] = array[j]
            j -= step

        array[j + step] = key

    return array


def shell_sort(array):
    step = 0
    while step <= len(array)//3+1:
        step = 3*step+1

    while step > 0:
        helper_insert(array, step)
        step = (step-1)//3

    return array


# DONE: quicksort - recursive, pivot = last el. of a seq.
def partition(array, low, high):
    pivot = array[high]  # pivot chosen as the last element of a sequence
    i = low-1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quick_sort_recursive(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        pivot = partition(array, low, high)
        quick_sort_recursive(array, low, pivot - 1)
        quick_sort_recursive(array, pivot + 1, high)

    return array


def quick_sort(array):
    return quick_sort_recursive(array, 0, len(array)-1)
