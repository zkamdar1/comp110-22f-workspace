"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730476042"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next == None:
        return head.data
    else:
        return last(head.next)

        
def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of Node stored at a specific index or raises IndexError if index does not exist."""
    if head is None or (index) < 0:
        raise IndexError("Index is out of bounds on the list.")
    elif (index) == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns the max data value in linked list or raises ValueError if empty."""
    if head is None:
        raise ValueError("Cannot call max with none")
    elif head.next == None:
        return head.data
    else:
        if head.data > head.next.data:
            return max(Node(head.data, head.next.next))
        else:
            return max(Node(head.next.data, head.next.next))
        

def linkify(items: list[int]) -> Optional[Node]:
    """Returns linked list of Nodes with same values and order of input list."""
    if items == []:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns new linked list of Nodes whose values are the orignal values scaled by factor."""
    if head is None:
        return None
    elif head.next is None:
        return Node(head.data * factor, None)
    else:
        return Node(head.data * factor, scale(head.next, factor))

