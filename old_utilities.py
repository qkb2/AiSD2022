import random


def decreasing_generator(n: int, k: int) -> list:
    random.seed()
    random_list = [random.randint(9 * k // 10, k)]
    for i in range(0, n - 1):
        random_list.append(random_list[i] - random.randint(0, k // n))

    return random_list


# merge sort
def merge(left_array: list, right_array: list, array: list) -> None:
    # function merges both arrays together
    # next element to be added to the array is chosen from the smallest elements from both L and R arrays.
    # val. l and r increment every time their smaller element is merged (so that l and r always point towards the next
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

def merge_sort(array: list) -> list:
    if len(array) > 1:
        midway = len(array)//2
        left_array = array[:midway]
        right_array = array[midway:]
        # recursion - the array is split in the middle (mid-point)
        merge_sort(left_array)
        merge_sort(right_array)
        merge(left_array, right_array, array)

    return array


# heap sort
def heapify(array: list, parent_idx: int, heap_size: int) -> None:
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

def build_heap(array: list) -> list:
    # the len(array)//2-1 is the index of the last parent
    for i in range(len(array)//2-1, -1, -1):
        heapify(array, i, len(array))

    return array

def heap_sort(array: list) -> list:
    build_heap(array)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)

    return array


if __name__ == "__main__":
    nn = int(input("n: "))
    kk = int(input("k: "))
    print(decreasing_generator(nn, kk))  # using k = 10*n provides reasonable results
    print(merge_sort([2,1,3,7,4,2,0,6,9]))
    print(heap_sort([2,1,3,7,4,2,0,6,9]))
