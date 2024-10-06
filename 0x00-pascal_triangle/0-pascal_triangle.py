#!/usr/bin/python3
"""A script to determine Pascal's triangle for any number"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    # Get the Pascal's triangle for (n-1)
    triangle = pascal_triangle(n - 1)

    # Calculate the next row using the previous row
    last_row = triangle[-1]
    new_row = [1]

    for i in range(1, len(last_row)):
        new_row.append(last_row[i - 1] + last_row[i])

    new_row.append(1)
    triangle.append(new_row)

    return triangle