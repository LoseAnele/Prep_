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
    # Check if number is less than or equal to 1, which are not prime numbers
    if n <= 1:
        return False
    # Loop from 2 to square root of n to check for factors
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i, then it's not prime
        if n % i == 0:
            return False
    # If no factors found, n is prime
    return True

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
    # Initialize counter variable to 0
    count = 0
    # Loop through each character in the text after converting to lowercase
    for char in text.lower():
        # If character is a vowel, increment counter
        if char in 'aeiou':
            count += 1
    # Return total count of vowels
    return count

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
    # If list is empty, raise ValueError
    if not numbers:
        raise ValueError("List cannot be empty")
    # Return maximum value using built-in max function
    return max(numbers)

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
    # Initialize total sum to 0
    total = 0
    # Convert number to string and loop through each digit
    for digit in str(abs(number)):
        # Add integer value of digit to total
        total += int(digit)
    # Return sum of all digits
    return total

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
    # Return reversed string using slice notation with step -1
    return text[::-1]

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
    # Handle special case of 0 factorial
    if n == 0:
        return 1
    # Initialize result to 1
    result = 1
    # Multiply result by each number from 1 to n
    for i in range(1, n + 1):
        result *= i
    # Return factorial result
    return result

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
    # Return True if number is divisible by 2, False otherwise
    return n % 2 == 0

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
    # Initialize total sum to 0
    total = 0
    # Loop through each number in the list
    for num in numbers:
        # If number is even, add it to total
        if num % 2 == 0:
            total += num
    # Return sum of even numbers
    return total

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
    # Use built-in count method to count occurrences of char in text
    return text.count(char)

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
    # Convert list to set to remove duplicates and sort in descending order
    unique_sorted = sorted(set(numbers), reverse=True)
    # If less than 2 unique numbers, raise error
    if len(unique_sorted) < 2:
        raise ValueError("All numbers are identical")
    # Return second element (second largest)
    return unique_sorted[1]

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
    # Return True if year is divisible by 4 and either not divisible by 100 or divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

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
    # Remove spaces and convert to lowercase for str1
    str1 = ''.join(str1.lower().split())
    # Remove spaces and convert to lowercase for str2
    str2 = ''.join(str2.lower().split())
    # Return True if sorted characters are equal
    return sorted(str1) == sorted(str2)

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
    # Initialize total sum to 0
    total = 0
    # Loop through list with step 2 to get even indices
    for i in range(0, len(numbers), 2):
        # Add number at even index to total
        total += numbers[i]
    # Return sum of numbers at even indices
    return total

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
    # If string is empty, raise error
    if not text:
        raise ValueError("String cannot be empty")
    # Calculate middle index
    mid = len(text) // 2
    # Return two middle characters if length is even, one if odd
    return text[mid-1:mid+1] if len(text) % 2 == 0 else text[mid]

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
    # If sentence is empty, raise error
    if not sentence:
        raise ValueError("Sentence cannot be empty")
    # Split sentence into words
    words = sentence.split()
    # Initialize longest word as first word
    longest = words[0]
    # Loop through remaining words
    for word in words[1:]:
        # Update longest if current word is longer
        if len(word) > len(longest):
            longest = word
    # Return longest word found
    return longest

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
    # Initialize empty result list
    result = []
    # Loop count times
    for i in range(1, count + 1):
        # Append multiple of n to result
        result.append(n * i)
    # Return list of multiples
    return result

def two_sum(nums, target):
    """
        Write a program that accepts two parameters nums and target.
        The program should get the two indexes that sum up to the target.
        Return the indexes in a list format.
        [1,2,3,4,5], 9 = [3, 4]
    """
    # Initialize dictionary to store seen numbers
    seen = {}
    # Loop through list with index and value
    for i, num in enumerate(nums):
        # Calculate complement needed to reach target
        complement = target - num
        # If complement exists in seen dictionary, return indices
        if complement in seen:
            return [seen[complement], i]
        # Store current number and index
        seen[num] = i
    # Return empty list if no solution found
    return []

def is_palindrome(word):
    """
        A palindrome is a word, phrase, number, or sequence that 
        reads the same forward and backward, ignoring spaces, punctuation, and capitalization
        Create a program that accepts one parameter word, 
        return True if word is palindrome else returns False 
    """
    # Compare word with its reverse
    return word == word[::-1]

def fibonacci(num: int):
    """
        The Fibonacci sequence is a series of numbers 
        in which each number is the sum of the two preceding ones, 
        usually starting with 0 and 1. 
        Create a program that accepts one parameter num and returns 
    """
    # Handle base cases
    if num <= 1:
        return num
    # Initialize first two numbers
    prev, curr = 0, 1
    # Calculate fibonacci number through iteration
    for _ in range(2, num + 1):
        prev, curr = curr, prev + curr
    # Return final fibonacci number
    return curr

def find_duplicates(array: list):
    """
        Create a program that accepts one parameter array 
        and returns a list of duplicates in the array
    """
    # Initialize sets for seen and duplicate numbers
    seen = set()
    duplicates = set()
    # Loop through array
    for num in array:
        # If number already seen, add to duplicates
        if num in seen:
            duplicates.add(num)
        # Add number to seen set
        seen.add(num)
    # Convert duplicates set to list and return
    return list(duplicates)

""" Searching Algorithms """
def binary_search(array: list, target: int):
    """
        Binary search is an efficient algorithm for finding a 
        target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts two parameters array and target, 
        uses the binary search algorithm to return an index of the target number, -1 if not found.
    """
    # Initialize left and right pointers
    left, right = 0, len(array) - 1
    # Continue while search space exists
    while left <= right:
        # Calculate middle index
        mid = (left + right) // 2
        # If target found, return index
        if array[mid] == target:
            return mid
        # If middle element is less than target, search right half
        elif array[mid] < target:
            left = mid + 1
        # If middle element is greater than target, search left half
        else:
            right = mid - 1
    # Return -1 if target not found
    return -1

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
    # Loop through array with index
    for i in range(len(arr)):
        # If current element matches target, return its index
        if arr[i] == target:
            return i
    # Return -1 if target not found
    return -1

""" Sorting Algorithms """
def bubble_sort(array: list):
    """
        Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts one parameter array and returns a sorted array using bubble sort algorithm.
        
        :param array: A list of integers to be sorted.
        :return: A sorted list of integers.
    """
    # Get length of array
    n = len(array)
    # Outer loop for passes
    for i in range(n):
        # Inner loop for comparisons
        for j in range(0, n - i - 1):
            # If current element is greater than next element, swap them
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    # Return sorted array
    return array

def merge_sort(array: list):
    """
        Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts one parameter array and returns a sorted array using merge sort algorithm.
        
        :param array: A list of integers to be sorted.
        :return: A sorted list of integers.
    """
    # Base case: if array has 1 or fewer elements, return it
    if len(array) <= 1:
        return array
    # Calculate middle index
    mid = len(array) // 2
    # Split array into left and right halves
    left_half = array[:mid]
    right_half = array[mid:]
    # Recursively sort and merge halves
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left: list, right: list):
    """
        Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts two parameters left and right and returns a merged sorted array.
        
        :param left: The first sorted list.
        :param right: The second sorted list.
        :return: A single sorted list containing elements from both input lists.
    """
    # Initialize merged result list
    merged = []
    # Initialize indices for both lists
    left_index = 0
    right_index = 0
    # Compare elements from both lists and merge
    while left_index < len(left) and right_index < len(right):
        # If left element is smaller or equal, add it to merged list
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        # If right element is smaller, add it to merged list
        else:
            merged.append(right[right_index])
            right_index += 1
    # Add remaining elements from left list
    merged.extend(left[left_index:])
    # Add remaining elements from right list
    merged.extend(right[right_index:])
    # Return merged sorted list
    return merged

def quicksort(array: list):
    """
        Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half. 
        It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

        Create a program that accepts one parameter array and returns a sorted array using quicksort algorithm.
        
        :param array: A list of integers to be sorted.
        :return: A sorted list of integers.
    """
    # Base case: if array has 1 or fewer elements, return it
    if len(array) <= 1:
        return array
    # Choose middle element as pivot
    pivot = array[len(array) // 2]
    # Create lists for elements less than pivot
    left = [x for x in array if x < pivot]
    # Create list for elements equal to pivot
    middle = [x for x in array if x == pivot]
    # Create list for elements greater than pivot
    right = [x for x in array if x > pivot]
    # Recursively sort and combine lists
    return quicksort(left) + middle + quicksort(right)

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
    # Initialize empty list for squared values
    squared_list = []
    # Loop through input list
    for x in arr:
        # Append squared value to result list
        squared_list.append(x**2)
    # Return list of squared values
    return squared_list

def even_numbers(arr: list):
    """
        Even numbers function filters a list to only keep even numbers.
        It iterates through the input list and checks each number for divisibility by 2.

        Create a program that accepts one parameter arr and returns a list with even numbers.
        
        :param arr: A list of integers to be filtered.
        :return: A list containing only even numbers.
    """
    # Initialize empty list for even numbers
    even_list = []
    # Loop through input list
    for x in arr:
        # If number is even, append to result list
        if x % 2 == 0:
            even_list.append(x)
    # Return list of even numbers
    return even_list

def flattened(arr: list):
    """
        Flattened function converts a nested list into a single-level list.
        It iterates through each sublist and adds individual elements to a new list.

        Create a program that accepts one parameter arr and returns a flattened list.
        
        :param arr: A nested list of integers.
        :return: A flattened list containing all elements.
    """
    # Initialize empty list for flattened result
    flattened_list = []
    # Loop through each sublist in input list
    for sublist in arr:
        # Loop through each item in sublist
        for item in sublist:
            # Append item to flattened list
            flattened_list.append(item)
    # Return flattened list
    return flattened_list

def extend(arr: list, ext: list):
    """
        Extend function combines two lists by adding all elements from the second list
        to the end of the first list. This modifies the original list in-place.

        Create a program that accepts two parameters arr and ext and returns an extended list.
        
        :param arr: The original list to be extended.
        :param ext: The list to extend with.
        :return: The extended list.
    """
    # Extend first list with second list
    arr.extend(ext)
    # Return extended list
    return arr

def reverse(arr: list):
    """
        Reverse function changes the order of elements in a list to be backwards.
        This operation is performed in-place, modifying the original list.

        Create a program that accepts one parameter arr and returns a reversed list.
        
        :param arr: A list to be reversed.
        :return: The reversed list.
    """
    # Reverse list in place
    arr.reverse()
    # Return reversed list
    return arr

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
    # Define second set
    other_set = {4, 5, 6, 7}
    # Return symmetric difference of two sets
    return set1.symmetric_difference(other_set)

def subset():
    """
    Create a subset that is guaranteed to be a subset of {1, 2, 3, 4, 5}.
    
    Returns:
        set: A set that is a subset of {1, 2, 3, 4, 5}
        
    Example:
        >>> subset()
        {1, 2, 3}
    """
    # Return a subset of {1, 2, 3, 4, 5}
    return {1, 2, 3}

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
    # Return union of regular set and frozen set
    return sample_set.union(frozen_set)

def is_disjoint(set1, set2):
    """
    Check if two sets are disjoint (have no elements in common).
    
    Args:
        set1 (set): First set to compare
        set2 (set): Second set to compare
        
    Returns:
        bool: True if sets are disjoint, False otherwise
        
    Example:
        >>> is_disjoint({1, 2, 3}, {4, 5, 6})
        True
    """
    # Return True if sets have no elements in common
    return set1.isdisjoint(set2)