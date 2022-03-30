import sorts_with_counters
import generator


if __name__ == '__main__':
    arr = generator.random_generator(1000)
    merge = sorts_with_counters.merge_sort_wrapper(arr.copy())
    heap = sorts_with_counters.heap_sort_wrapper(arr.copy())
    insert = sorts_with_counters.insertion_sort_wrapper(arr.copy())
    shell = sorts_with_counters.shell_sort_wrapper(arr.copy())
    quick = sorts_with_counters.quick_sort_wrapper(arr.copy())
    print(merge, heap, insert, shell, quick, sep="\n\n")