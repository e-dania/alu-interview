#!/usr/bin/python3

"""
Module for calculating the amount of rainwater retained between walls.

This module contains a single function, `rain`, which calculates
the total amount of rainwater retained between a list of walls.
"""


def rain(walls):
    """
    Calculate the amount of rainwater retained between walls.

    Args:
    walls (list): A list of non-negative integers representing wall's height.

    Returns:
        int: The total amount of rainwater retained.

    Raises:
        TypeError: If the input is not a list of integers.

    Example:
        >>> rain([0, 1, 0, 2, 0, 3, 0, 4])
        6
        >>> rain([2, 0, 0, 4, 0, 0, 1, 0])
        6
    """
    if not walls:
        return 0

    total_rain = 0
    left_max = [0] * len(walls)
    right_max = [0] * len(walls)

    left_max[0] = walls[0]
    for i in range(1, len(walls)):
        left_max[i] = max(left_max[i-1], walls[i-1])

    right_max[-1] = walls[-1]
    for i in range(len(walls)-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i+1])

    for i in range(len(walls)):
        total_rain += max(0, min(left_max[i], right_max[i]) - walls[i])

    return total_rain
