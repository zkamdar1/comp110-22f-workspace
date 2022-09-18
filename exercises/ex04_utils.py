"""EX04 - Practicing computational thinking through algorithms."""

__author__ = "730476042"

# Function name: all
# Function parameters: package list([int]), number (int))
# Return type: bool
def all(package: list([int]), number: int) -> bool:
    """Returns True if every index in packages equals number."""
    # Gameplan:
    # 1. Start with first index
    i: int = 0
    # 2. Loop through every index 
    while i < len(package) or len(package) == 0:
        # 2.A. Test to see if list is empty or number equals index
        if package == [] or number != package[i]:
            return False
        else:
        #  2.A. Test to see if every index is equal to number
            i += 1
    return True


# Function name: max
# Function parameters: list([int])
# Return type: int
def max(input: list[int]) -> int:
    """Returns the largest int found in list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # Gameplan
    # Need to loop through every index, comparing the current largest with the next index, and assigning the current largest to the large value between the two indexes
    big = 0
    i: int = 1

    while i < len(input):
        if input[big] > input[i]:
            i += 1
        else:
            big = i
            i += 1
    return input[big]


# Function name: is_equal
# Function parameters: list1 list([int]), list2 list([int])
# Return type: bool
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if all elements at every index are equal."""
    i_one: int = 0
    i_two: int = 0

    while i_one < len(list1) and i_two < len(list2):
        if list1[i_one] != list2[i_two]:
            return False
        i_one += 1
        i_two += 1
    return True
