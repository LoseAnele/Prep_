import unittest
import functions

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(functions.is_prime(7))
    
    def test_non_prime_number(self):
        self.assertFalse(functions.is_prime(4))
    
    def test_edge_case_one(self):
        self.assertFalse(functions.is_prime(1))
    
    def test_large_prime_number(self):
        self.assertTrue(functions.is_prime(29))
    
    def test_negative_number(self):
        self.assertFalse(functions.is_prime(-3))

class TestCountVowels(unittest.TestCase):
    def test_mixed_case_string(self):
        self.assertEqual(functions.count_vowels("Hello World"), 3)
    
    def test_empty_string(self):
        self.assertEqual(functions. count_vowels(""), 0)
    
    def test_no_vowels(self):
        self.assertEqual(functions.count_vowels("bcdfg"), 0)
    
    def test_all_vowels(self):
        self.assertEqual(functions.count_vowels("aeiouAEIOU"), 10)

class TestFindMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(functions.find_max([1, 5, 3, 9, 2]), 9)
    
    def test_negative_numbers(self):
        self.assertEqual(functions.find_max([-1, -5, -3, -9, -2]), -1)
    
    def test_single_element(self):
        self.assertEqual(functions.find_max([4]), 4)
    
    def test_mixed_numbers(self):
        self.assertEqual(functions.find_max([10, -2, 3, 15, 7]), 15)

class TestSumDigits(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(functions.sum_digits(1234), 10)
    
    def test_single_digit(self):
        self.assertEqual(functions.sum_digits(7), 7)
    
    def test_large_number(self):
        self.assertEqual(functions.sum_digits(98765), 35)
    
    def test_zero(self):
        self.assertEqual(functions.sum_digits(0), 0)

class TestReverseString(unittest.TestCase):
    def test_regular_string(self):
        self.assertEqual(functions.reverse_string("hello"), "olleh")
    
    def test_empty_string(self):
        self.assertEqual(functions.reverse_string(""), "")
    
    def test_palindrome_string(self):
        self.assertEqual(functions.reverse_string("radar"), "radar")
    
    def test_with_spaces(self):
        self.assertEqual(functions.reverse_string("Hello World"), "dlroW olleH")

class TestFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(functions.factorial(0), 1)
    
    def test_factorial_of_one(self):
        self.assertEqual(functions.factorial(1), 1)
    
    def test_small_number(self):
        self.assertEqual(functions.factorial(5), 120)
    
    def test_large_number(self):
        self.assertEqual(functions.factorial(7), 5040)

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(functions.is_even(10))
    
    def test_odd_number(self):
        self.assertFalse(functions.is_even(7))
    
    def test_zero(self):
        self.assertTrue(functions.is_even(0))
    
    def test_negative_even_number(self):
        self.assertTrue(functions.is_even(-4))

class TestSumEvenNumbers(unittest.TestCase):
    def test_list_with_evens(self):
        self.assertEqual(functions.sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)
    
    def test_list_with_no_evens(self):
        self.assertEqual(functions.sum_even_numbers([1, 3, 5, 7]), 0)
    
    def test_empty_list(self):
        self.assertEqual(functions.sum_even_numbers([]), 0)
    
    def test_all_even_numbers(self):
        self.assertEqual(functions.sum_even_numbers([2, 4, 6, 8]), 20)

class TestCountCharacter(unittest.TestCase):
    def test_count_regular_char(self):
        self.assertEqual(functions.count_char("hello world", 'l'), 3)
    
    def test_char_not_in_string(self):
        self.assertEqual(functions.count_char("hello", 'z'), 0)
    
    def test_empty_string(self):
        self.assertEqual(functions.count_char("", 'a'), 0)
    
    def test_case_sensitivity(self):
        self.assertEqual(functions.count_char("Hello", 'h'), 0)
        self.assertEqual(functions.count_char("Hello", 'H'), 1)

class TestSecondLargest(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(functions.second_largest([3, 1, 4, 1, 5, 9, 2]), 5)
    
    def test_list_with_duplicates(self):
        self.assertEqual(functions.second_largest([1, 3, 3, 3, 2]), 2)
    
    def test_list_with_two_numbers(self):
        self.assertEqual(functions.second_largest([10, 5]), 5)
    
    def test_identical_numbers(self):
        with self.assertRaises(ValueError):
            functions.second_largest([3, 3, 3])

class TestIsLeapYear(unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(functions.is_leap_year(2020))
    
    def test_non_leap_year(self):
        self.assertFalse(functions.is_leap_year(2019))
    
    def test_century_non_leap_year(self):
        self.assertFalse(functions.is_leap_year(1900))
    
    def test_century_leap_year(self):
        self.assertTrue(functions.is_leap_year(2000))

class TestIsAnagram(unittest.TestCase):
    def test_anagram_words(self):
        self.assertTrue(functions.is_anagram("listen", "silent"))
    
    def test_non_anagram_words(self):
        self.assertFalse(functions.is_anagram("hello", "world"))
    
    def test_different_lengths(self):
        self.assertFalse(functions.is_anagram("hello", "helloo"))
        
    def test_anagrams_with_spaces(self):
        self.assertTrue(functions.is_anagram("dormitory", "dirty room"))  


class TestSumEvenIndices(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(functions.sum_even_indices([1, 2, 3, 4, 5, 6]), 9)
    
    def test_single_element_list(self):
        self.assertEqual(functions.sum_even_indices([5]), 5)
    
    def test_empty_list(self):
        self.assertEqual(functions.sum_even_indices([]), 0)
    
    def test_negative_numbers(self):
        self.assertEqual(functions.sum_even_indices([-1, -2, -3, -4, -5]), -9)

class TestMiddleCharacter(unittest.TestCase):
    def test_odd_length_string(self):
        self.assertEqual(functions.middle_character("hello"), "l")
    
    def test_even_length_string(self):
        self.assertEqual(functions.middle_character("test"), "es")
    
    def test_single_character_string(self):
        self.assertEqual(functions.middle_character("a"), "a")
    
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            functions.middle_character("")

class TestLongestWord(unittest.TestCase):
    def test_regular_sentence(self):
        self.assertEqual(functions.longest_word("The quick brown fox is kicking the lazy dog"), "kicking")
    
    def test_single_word(self):
        self.assertEqual(functions.longest_word("Hello"), "Hello")
    
    def test_multiple_words_same_length(self):
        self.assertEqual(functions.longest_word("dog cat bat"), "dog")
    
    def test_empty_sentence(self):
        with self.assertRaises(ValueError):
            functions.longest_word("")

class TestGenerateMultiples(unittest.TestCase):
    def test_multiples_of_3(self):
        self.assertEqual(functions.generate_multiples(3, 5), [3, 6, 9, 12, 15])
    
    def test_multiples_of_1(self):
        self.assertEqual(functions.generate_multiples(1, 4), [1, 2, 3, 4])
    
    def test_zero_multiples(self):
        self.assertEqual(functions.generate_multiples(7, 0), [])


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
        self.sorted_list = [11,12,22,25,34,64,90]
        self.empty_list = []
        self.single_element_list = [1]
        self.duplicate_list = [1,2,3,1,2,3,4,5,6]
        self.sorted_duplicate_list = [1,1,2,2,3,3,4,5,6]

    def test_bubble_sort(self):
        self.assertEqual(functions.bubble_sort(self.unsorted_list), self.sorted_list)
        self.assertEqual(functions.bubble_sort(self.empty_list), [])
        self.assertEqual(functions.bubble_sort(self.single_element_list), [1])
        self.assertEqual(functions.bubble_sort(self.duplicate_list), self.sorted_duplicate_list)
    
    def test_merge_sort(self):
        self.assertEqual(functions.merge_sort(self.unsorted_list), self.sorted_list)
        self.assertEqual(functions.merge_sort(self.empty_list), [])
        self.assertEqual(functions.merge_sort(self.single_element_list), [1])
        self.assertEqual(functions.merge_sort(self.duplicate_list), self.sorted_duplicate_list)
    
    def test_quicksort(self):
        self.assertEqual(functions.quicksort(self.unsorted_list), self.sorted_list)
        self.assertEqual(functions.quicksort(self.empty_list), [])
        self.assertEqual(functions.quicksort(self.single_element_list), [1])
        self.assertEqual(functions.quicksort(self.duplicate_list), self.sorted_duplicate_list)


class TestListOperations(unittest.TestCase):
    def setUp(self):
        self.sample_list = [1, 2, 3, 4, 5]
        self.nested_list = [[1, 2], [3, 4], [5, 6]]

    def test_list_comprehension(self):
        self.assertEqual(functions.square_list(self.sample_list), [1, 4, 9, 16, 25])

    def test_filter_list(self):
        self.assertEqual(functions.even_numbers(self.sample_list), [2, 4])

    def test_flatten_nested_list(self):
        self.assertEqual(functions.flattened(self.nested_list), [1, 2, 3, 4, 5, 6])

    def test_list_extend(self):
        self.assertEqual(functions.extend(self.sample_list, [6,7,8]), [1, 2, 3, 4, 5, 6, 7, 8])

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
