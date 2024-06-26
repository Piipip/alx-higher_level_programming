#!/usr/bin/python3
"""
Python script that contains a function to find a peak in a list of unsorted integers using binary search.
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.

    Args:
    - list_of_integers: A list of integers.

    Returns:
    - A peak element from the list.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]

