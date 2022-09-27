"""Implement function skeletons and implementations."""

__author__ = "730476042"


def only_evens(x: list[int]) -> list:
    """Returns only the even intergers found in given list."""
    i: int = 0
    even = []

    while i < len(x):
        if x[i] % 2 == 0:
            even.append(x[i])
        i += 1
    return even


def concat(xa: list[int], xb: list[int]) -> list:
    """Returns a list containing first list followed by second list."""
    i: int = 0
    new: list[int] = []

    while i < len(xa):
        new.append(xa[i])
        i += 1

    counter: int = 0

    while counter < len(xb):
        new.append(xb[counter])
        counter += 1
    return new


def sub(za: list[int], start: int, end: int) -> list:
    """Returns a list with values from start to end depending on end and start value."""
    sub_list: list[int] = []

    if len(za) == 0 or start >= len(za) or end <= 0:
        return sub_list
    if end > len(za):
        end = len(za) - 1
    else:
        end = end - 1
    if start < 0:
        start = 0
    sub_list.append(za[start])

    i: int = start + 1

    while i < end:
        sub_list.append(za[i])
        i += 1
    sub_list.append(za[end])

    return sub_list
