import unittest
import functions

class TestTwoSum(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(functions.two_sum([2,7,11,15], 9), [0, 1])
    def test_case_2(self):
        self.assertEqual(functions.two_sum([3,2,4], 6), [1, 2])
    def test_case_3(self):
        self.assertEqual(functions.two_sum([3,3], 6), [0, 1])
    def test_case_4(self):
        self.assertEqual(functions.two_sum([1,2,3,4], 9), [])

class TestBinarySearch(unittest.TestCase):
    def test_not_found(self):
        self.assertEqual(functions.binary_search([2,7,11,15], 9), -1)
    def test_found(self):
        self.assertEqual(functions.binary_search([1,2,3,4,5], 3), 2)
    def test_first_element(self):
        self.assertEqual(functions.binary_search([1,2,3,4,5], 1), 0)
    def test_last_element(self):
        self.assertEqual(functions.binary_search([1,2,3,4], 4), 3)

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(functions.is_palindrome("racecar"))
    def test_not_palindrom(self):
        self.assertFalse(functions.is_palindrome("hello"))

class TestFibonacci(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(functions.fibonacci(0), 0)
        self.assertEqual(functions.fibonacci(1), 1)
        self.assertEqual(functions.fibonacci(5), 5)
        self.assertEqual(functions.fibonacci(10), 55)

class TestFindDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertEqual(functions.find_duplicates([1,2,3,4,5]), [])
    def test_with_duplicates(self):
        self.assertEqual(sorted(functions.find_duplicates([1,2,3,2,4,5,1,6])), [1,2])

class TestBubbleSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(functions.bubble_sort([]), [])
    def test_single_element_list(self):
        self.assertEqual(functions.bubble_sort([1]), [1])
    def test_already_sorted_list(self):
        self.assertEqual(functions.bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    def test_reverse_sorted_list(self):
        self.assertEqual(functions.bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    def test_unsorted_list(self):
        self.assertEqual(functions.bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    def test_list_with_duplicates(self):
        self.assertEqual(functions.bubble_sort([5, 1, 4, 2, 8, 5, 2]), [1, 2, 2, 4, 5, 5, 8])


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.unsorted_list = [64,34,25,12,22,11,90]

    def test_symmetric_difference(self):
        self.assertEqual(functions.sym_diff(self.sample_set), {1, 2, 3, 6, 7})

    def test_subset(self):
        self.assertTrue(functions.subset().issubset(self.sample_set))

    def test_frozen_set_operations(self):
        self.assertEqual(functions.union_with_frozen(self.sample_set, self.frozen_set), {1, 2, 3, 4, 5})

    def test_disjoint_sets(self):
        self.sorted_list = [11,12,22,25,34,64,90]
        self.empty_list = []
        self.single_element_list = [1]
        self.dulicate_list = [3,1,2,3,3,2,1]
        self.sorted_duplicate_list = [1,1,2,2,3,3,3]

    def test_bubble_sort(self):
        self.assertEqual(functions.bubble_sort(self.unsorted_list), self.sorted_list)
        self.assertEqual(functions.bubble_sort(self.empty_list), [])
        self.assertEqual(functions.bubble_sort(self.single_element_list), [1])
        self.assertEqual(functions.bubble_sort(self.dulicate_list), self.sorted_duplicate_list)
    
    def test_merge_sort(self):
        self.assertEqual(functions.merge_sort(self.unsorted_list), self.sorted_list)
        self.assertEqual(functions.merge_sort(self.empty_list), [])
        self.assertEqual(functions.merge_sort(self.single_element_list), [1])
        self.assertEqual(functions.merge_sort(self.dulicate_list), self.sorted_duplicate_list)
    
    def test_quicksort(self):
        self.assertEqual(functions.quicksort(self.unsorted_list), self.sorted_list)
        self.assertEqual(functions.quicksort(self.empty_list), [])
        self.assertEqual(functions.quicksort(self.single_element_list), [1])
        self.assertEqual(functions.quicksort(self.dulicate_list), self.sorted_duplicate_list)


class TestListOperations(unittest.TestCase):
    def setUp(self):
        self.sample_list = [1, 2, 3, 4, 5]
        self.nested_list = [[1, 2], [3, 4], [5, 6]]


    def test_symmetric_difference(self):
        self.assertEqual(functions.sym_diff(self.sample_set), {1, 2, 3, 6, 7})

    def test_subset(self):
        self.assertTrue(functions.subset().issubset(self.sample_set))

    def test_frozen_set_operations(self):
        self.assertEqual(functions.union_with_frozen(self.sample_set, self.frozen_set), {1, 2, 3, 4, 5})

    def test_list_comprehension(self):
        self.assertEqual(functions.square_list(self.sample_list), [1, 4, 9, 16, 25])

    def test_filter_list(self):
        self.assertEqual(functions.even_numbers(self.sample_list), [2, 4])

    def test_flatten_nested_list(self):
        self.assertEqual(functions.flattened(self.nested_list), [1, 2, 3, 4, 5, 6])

    def test_list_extend(self):
        self.sample_list.extend([6, 7, 8])
        self.assertEqual(functions.extend(self.sample_list, [6,7,8]), [1, 2, 3, 4, 5, 6, 7, 8])


    def test_symmetric_difference(self):
        self.assertEqual(functions.sym_diff(self.sample_set), {1, 2, 3, 6, 7})

    def test_subset(self):
        self.assertTrue(functions.subset().issubset(self.sample_set))

    def test_frozen_set_operations(self):
        self.assertEqual(functions.union_with_frozen(self.sample_set, self.frozen_set), {1, 2, 3, 4, 5})

    def test_reverse_in_place(self):
        self.assertEqual(functions.reverse(self.sample_list), [5, 4, 3, 2, 1])

class TestSetOperations(unittest.TestCase):
    def setUp(self):
        self.sample_set = {1, 2, 3, 4, 5}
        self.other_set = {4, 5, 6, 7}
        self.frozen_set = frozenset([1, 2, 3])

    def test_symmetric_difference(self):
        self.assertEqual(functions.sym_diff(self.sample_set), {1, 2, 3, 6, 7})

    def test_subset(self):
        self.assertTrue(functions.subset().issubset(self.sample_set))

    def test_frozen_set_operations(self):
        self.assertEqual(functions.union_with_frozen(self.sample_set, self.frozen_set), {1, 2, 3, 4, 5})

    def test_disjoint_sets(self):
        disjoint_set = {8, 9, 10}
        self.assertTrue(self.sample_set.isdisjoint(disjoint_set))


    def test_symmetric_difference(self):
        self.assertEqual(functions.sym_diff(self.sample_set), {1, 2, 3, 6, 7})

    def test_subset(self):
        self.assertTrue(functions.subset().issubset(self.sample_set))

    def test_frozen_set_operations(self):
        self.assertEqual(functions.union_with_frozen(self.sample_set, self.frozen_set), {1, 2, 3, 4, 5})

    def test_disjoint_sets(self):
        self.assertEqual(self.sample_set, {4, 5})

    def test_symmetric_difference(self):
        self.assertEqual(functions.sym_diff(self.sample_set), {1, 2, 3, 6, 7})

    def test_subset(self):
        self.assertTrue(functions.subset().issubset(self.sample_set))

    def test_frozen_set_operations(self):
        self.assertEqual(functions.union_with_frozen(self.sample_set, self.frozen_set), {1, 2, 3, 4, 5})