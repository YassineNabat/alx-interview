#!/usr/bin/python3
"""
Contains a recursive method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""



def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly
    n H characters in the file, using recursion.
    """
    divisor=2
    if n <= 1:
        return 0

    if n % divisor == 0:
        return divisor + minOperations(n // divisor, divisor)
        
    return minOperations(n, divisor + 1)
