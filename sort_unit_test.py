import unittest
import sys

import sorts
import generator

sys.setrecursionlimit(10**6) #for quicksort which must be recursive

class SortsBasicTests(unittest.TestCase):
    array0 = [1]
    array1 = [2, 1, 3, 7, 4, 2, 0, 6, 9]
    solved1 = sorted(array1)
    array2 = [2, 1, 3, 7, 4, 2, 6, 9]
    solved2 = sorted(array2)
    array = generator.random_generator(1000)
    solved = sorted(array)

    def test_merge(self):
        self.assertEqual(sorts.merge_sort(self.array0), [1], "arr0 wrong")
        self.assertEqual(sorts.merge_sort(self.array1), self.solved1, "arr1 wrong")
        self.assertEqual(sorts.merge_sort(self.array2), self.solved2, "arr2 wrong")
        self.assertEqual(sorts.merge_sort(self.array), self.solved, "random array wrong")

    def test_heap(self):
        self.assertEqual(sorts.heap_sort(self.array0), [1], "arr0 wrong")
        self.assertEqual(sorts.heap_sort(self.array1), self.solved1, "arr1 wrong")
        self.assertEqual(sorts.heap_sort(self.array2), self.solved2, "arr2 wrong")
        self.assertEqual(sorts.heap_sort(self.array), self.solved, "random array wrong")

    def test_quick(self):
        self.assertEqual(sorts.quick_sort(self.array0), [1], "arr0 wrong")
        self.assertEqual(sorts.quick_sort(self.array1), self.solved1, "arr1 wrong")
        self.assertEqual(sorts.quick_sort(self.array2), self.solved2, "arr2 wrong")
        self.assertEqual(sorts.quick_sort(self.array), self.solved, "random array wrong")

    def test_shell(self):
        self.assertEqual(sorts.shell_sort(self.array0), [1], "arr0 wrong")
        self.assertEqual(sorts.shell_sort(self.array1), self.solved1, "arr1 wrong")
        self.assertEqual(sorts.shell_sort(self.array2), self.solved2, "arr2 wrong")
        self.assertEqual(sorts.shell_sort(self.array), self.solved, "random array wrong")

    def test_insert(self):
        self.assertEqual(sorts.insertion_sort(self.array0), [1], "arr0 wrong")
        self.assertEqual(sorts.insertion_sort(self.array1), self.solved1, "arr1 wrong")
        self.assertEqual(sorts.insertion_sort(self.array2), self.solved2, "arr2 wrong")
        self.assertEqual(sorts.insertion_sort(self.array), self.solved, "random array wrong")

    def nothing_wrong(self):
        self.assertEqual(self.array1,[2, 1, 3, 7, 4, 2, 0, 6, 9], "arr1 changed")
        self.assertEqual(self.array2, [2, 1, 3, 7, 4, 2, 6, 9], "arr2 changed")


#class ActualTests(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
