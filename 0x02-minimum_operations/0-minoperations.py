#!/usr/bin/python3
"""
Contains a recursive method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperationsRecursive(n, divisor=2):
    """
    Returns the fewest number of operations needed to result in exactly
    n H characters in the file, using recursion.
    """
    if n <= 1:
        return 0

    if n % divisor == 0:
        return divisor + minOperationsRecursive(n // divisor, divisor)
        
    return minOperationsRecursive(n, divisor + 1)
