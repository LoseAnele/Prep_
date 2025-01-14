"""  """
def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
        
    Example:
        >>> is_prime(7)
        True
    """
    pass

def count_vowels(text):
    """
    Count the number of vowels in a string.
    
    Args:
        text (str): The string to check
        
    Returns:
        int: The number of vowels in the string
        
    Example:
        >>> count_vowels("Hello World")
        3
    """
    pass

def find_max(numbers):
    """
    Find the maximum number in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int: The maximum number in the list
        
    Example:
        >>> find_max([1, 5, 3, 9, 2])
        9
    """
    pass

def sum_digits(number):
    """
    Calculate the sum of digits in a number.
    
    Args:
        number (int): The number to sum digits from
        
    Returns:
        int: Sum of all digits
        
    Example:
        >>> sum_digits(1234)
        10
    """
    pass

def reverse_string(text):
    """
    Reverse a string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    pass

def factorial(n):
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of the number
        
    Example:
        >>> factorial(5)
        120
    """
    pass

def is_even(n):
    """
    Check if a number is even.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is even, False otherwise
        
    Example:
        >>> is_even(10)
        True
    """
    pass

def sum_even_numbers(numbers):
    """
    Calculate the sum of even numbers in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int: Sum of all even numbers
        
    Example:
        >>> sum_even_numbers([1, 2, 3, 4, 5, 6])
        12
    """
    pass

def count_char(text, char):
    """
    Count occurrences of a character in a string.
    
    Args:
        text (str): The string to search in
        char (str): The character to count
        
    Returns:
        int: Number of occurrences of the character
        
    Example:
        >>> count_char("hello world", 'l')
        3
    """
    pass

def second_largest(numbers):
    """
    Find the second largest number in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int: The second largest number
        
    Raises:
        ValueError: If all numbers are identical
        
    Example:
        >>> second_largest([3, 1, 4, 1, 5, 9, 2])
        5
    """
    pass

def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if it's a leap year, False otherwise
        
    Example:
        >>> is_leap_year(2020)
        True
    """
    pass

def is_anagram(str1, str2):
    """
    Check if two strings are anagrams.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
        
    Example:
        >>> is_anagram("listen", "silent")
        True
    """
    pass

def sum_even_indices(numbers):
    """
    Sum numbers at even indices in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int: Sum of numbers at even indices
        
    Example:
        >>> sum_even_indices([1, 2, 3, 4, 5, 6])
        9
    """
    pass

def middle_character(text):
    """
    Find the middle character(s) of a string.
    
    Args:
        text (str): The input string
        
    Returns:
        str: Middle character(s)
        
    Raises:
        ValueError: If string is empty
        
    Example:
        >>> middle_character("hello")
        "l"
    """
    pass

def longest_word(sentence):
    """
    Find the first longest word in a sentence.
    
    Args:
        sentence (str): The input sentence
        
    Returns:
        str: The longest word
        
    Raises:
        ValueError: If sentence is empty
        
    Example:
        >>> longest_word("The quick brown fox")
        "quick"
    """
    pass

def generate_multiples(n, count):
    """
    Generate a list of multiples of a number.
    
    Args:
        n (int): The number to find multiples of
        count (int): How many multiples to generate
        
    Returns:
        list: List of multiples
        
    Example:
        >>> generate_multiples(3, 5)
        [3, 6, 9, 12, 15]
    """
    pass

def two_sum(nums, target):
    """
        Write a program that accepts two parameters nums and target.
        The program should get the two indexes that sum up to the target.
        Return the indexes in a list format.
        [1,2,3,4,5], 9 = [3, 4]
    """
    pass

def is_palindrome(word):
    """
        A palindrome is a word, phrase, number, or sequence that 
        reads the same forward and backward, ignoring spaces, punctuation, and capitalization
        Create a program that accepts one parameter word, 
        return True if word is palindrome else returns False 
    """
    pass

def fibonacci(num: int):
    """
        The Fibonacci sequence is a series of numbers 
        in which each number is the sum of the two preceding ones, 
        usually starting with 0 and 1. 
        Create a program that accepts one parameter num and returns 
    """
    pass

def find_duplicates(array: list):
    """
        Create a program that accepts one parameter array 
        and returns a list of duplicates in the array
    """
    pass

""" Searching Algorithms """
def binary_search(array: list, target: int):
    """
        Binary search is an efficient algorithm for finding a 
        target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts two parameters array and target, 
        uses the binary search algorithm to return an index of the target number, -1 if not found.
    """
    pass

def linear_search(arr, target):
    """
        Linear search is a simple search algorithm that sequentially checks each element in a list
        until a match is found or the whole list has been searched.
        It works on both sorted and unsorted lists but is less efficient than binary search for sorted lists.

        Create a program that accepts two parameters arr and target,
        uses linear search to return the index of target if found, -1 if not found.
        
        :param arr: The list to search through
        :param target: The value to search for
        :return: Index of target if found, -1 if not found
    """
    pass

""" Sorting Algorithms """
def bubble_sort(array: list):
    """
        Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts one parameter array and returns a sorted array using bubble sort algorithm.
        
        :param array: A list of integers to be sorted.
        :return: A sorted list of integers.
    """
    pass

def merge_sort(array: list):
    """
        Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts one parameter array and returns a sorted array using merge sort algorithm.
        
        :param array: A list of integers to be sorted.
        :return: A sorted list of integers.
    """
    pass

def merge(left: list, right: list):
    """
        Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts two parameters left and right and returns a merged sorted array.
        
        :param left: The first sorted list.
        :param right: The second sorted list.
        :return: A single sorted list containing elements from both input lists.
    """
    pass

def quicksort(array: list):
    """
        Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts one parameter array and returns a sorted array using quicksort algorithm.
        
        :param array: A list of integers to be sorted.
        :return: A sorted list of integers.
    """
    pass

""" Data Structures """
""" List """
def square_list(arr: list):
    """
        Square list takes a list of numbers and returns a new list with each number squared.
        This is useful for mathematical operations that require squared values.

        Create a program that accepts one parameter arr and returns a list with squared values.
        
        :param arr: A list of integers to be squared.
        :return: A list with squared values.
    """
    pass

def even_numbers(arr: list):
    """
        Even numbers function filters a list to only keep even numbers.
        It iterates through the input list and checks each number for divisibility by 2.

        Create a program that accepts one parameter arr and returns a list with even numbers.
        
        :param arr: A list of integers to be filtered.
        :return: A list containing only even numbers.
    """
    pass

def flattened(arr: list):
    """
        Flattened function converts a nested list into a single-level list.
        It iterates through each sublist and adds individual elements to a new list.

        Create a program that accepts one parameter arr and returns a flattened list.
        
        :param arr: A nested list of integers.
        :return: A flattened list containing all elements.
    """
    pass

def extend(arr: list, ext: list):
    """
        Extend function combines two lists by adding all elements from the second list
        to the end of the first list. This modifies the original list in-place.

        Create a program that accepts two parameters arr and ext and returns an extended list.
        
        :param arr: The original list to be extended.
        :param ext: The list to extend with.
        :return: The extended list.
    """
    pass

def reverse(arr: list):
    """
        Reverse function changes the order of elements in a list to be backwards.
        This operation is performed in-place, modifying the original list.

        Create a program that accepts one parameter arr and returns a reversed list.
        
        :param arr: A list to be reversed.
        :return: The reversed list.
    """
    pass

def sym_diff(set1):
    """
    Calculate the symmetric difference between two sets.
    
    Args:
        set1 (set): The first set to compare
        
    Returns:
        set: A new set containing elements that are in either set1 or the other_set, but not in both
        
    Example:
        >>> sym_diff({1, 2, 3, 4, 5})
        {1, 2, 3, 6, 7}
    """
    pass

def subset():
    """
    Create a subset that is guaranteed to be a subset of {1, 2, 3, 4, 5}.
    
    Returns:
        set: A set that is a subset of {1, 2, 3, 4, 5}
        
    Example:
        >>> subset()
        {1, 2, 3}
    """
    pass

def union_with_frozen(sample_set, frozen_set):
    """
    Perform a union operation between a regular set and a frozen set.
    
    Args:
        sample_set (set): The regular set to perform union with
        frozen_set (frozenset): The frozen set to perform union with
        
    Returns:
        set: A new set containing all unique elements from both sets
        
    Example:
        >>> union_with_frozen({1, 2, 3, 4, 5}, frozenset([1, 2, 3]))
        {1, 2, 3, 4, 5}
    """
    pass
