
"""  """
def two_sum(nums: list, target: int):
    """
        Write a program that accepts two parameters nums and target.
        The program should get the two indexes that sum up to the target.
        Return the indexes in a list format.
        [1,2,3,4,5], 9 = [3, 4]
    """
    for i in range(len(nums)):
        if not i == len(nums) - 1:
           if nums[i] + nums[i + 1] == target:
               return [i, i + 1]
    
    return []      

def is_palindrome(word):
    """
        A palindrome is a word, phrase, number, or sequence that 
        reads the same forward and backward, ignoring spaces, punctuation, and capitalization
        Create a program that accepts one parameter word, 
        return True if word is palindrome else returns False 
    """
    return word == word[::-1]

def fibonacci(num: int):
    """
        The Fibonacci sequence is a series of numbers 
        in which each number is the sum of the two preceding ones, 
        usually starting with 0 and 1. 
        Create a program that accepts one parameter num and returns 
    """
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def find_duplicates(array: list):
    """
        Create a program that accepts one parameter array 
        and returns a list of duplicates in the array
    """
    _list = []
    i = 0
    while True:
        if not len(array) == 0:
            temp = array[i]
            array.remove(array[i])
            if temp in array:
                _list.append(temp)
        else:
            break
    return _list
    
find_duplicates([1,2,3,2,4,5,1,6])   
# """ Searching Algorithms """
# def binary_search(array: list, target: int):
#     """
#         Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search interval in half. 
#         It compares the target value to the middle element and eliminates half of the remaining elements until the target is found or the interval is empty.

#         Create a program that accepts two parameters array and target, 
#         uses the binary search algorithm to return an index of the target number, -1 if not found.
#     """
#     pass

# def linear_search(arr, target):

#     pass

# """ Sorting Algorithms """
# def bubble_sort(array: list):
#     pass

# def merge_sort(array: list):
#     pass

#     def merge(left: list, right: list):
#         pass

# def quicksort(array: list):
#     pass

# """ Data Structures """
# """ List """
# def square_list(arr: list):
#     pass
# def even_numbers(arr: list):
#     pass
# def flattened(arr: list):
#     pass
# def extend(arr: list, ext: list):
#     pass
# def reverse(arr: list):
#     pass