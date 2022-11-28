"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730476042"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_last_one_value() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, None)
    assert last(linked_list) == 1


def test_value_at_empty() -> None:
    """Value_at of an empty Linked List should raise a IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_non_empty() -> None:
    """Value_at should return the value at a specific index in non-empty list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_value_at_neg_index() -> None:
    """Value_at should raise IndexError if index is negative."""
    linked_list = Node(10, Node(20, Node(30, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, -1)


def test_max_empty() -> None:
    """Max of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty_end() -> None:
    """Max of a non-empty Linked List should return max value in list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30

    
def test_max_non_empty_mid() -> None:
    """Max should return max value in linked list regardless of index."""
    linked_list = Node(15, Node(20, Node(10, None)))
    assert max(linked_list) == 20


def test_max_non_empty_first() -> None:
    """Max should return max value in linked list regardless of index."""
    linked_list = Node(9, Node(6, Node(3, None)))
    assert max(linked_list) == 9

    
def test_linkify_empty() -> None:
    """Linkify should return None if given empty list."""
    int_list: list[int] = []
    assert linkify(int_list) == None


def test_linkify_non_empty() -> None:
    """Linkify should return new linked list in same order as list of ints given."""
    int_list: list[int] = [1, 2, 3]
    node: Node = Node(3, Node(2, Node(1, None)))
    assert print(linkify(int_list)) == print(node)


def test_linkify_random_non_empty() -> None:
    """Linkify should return new linked list in same order as list of ints given."""
    int_list: list[int] = [1, 2, 3, 3, 2, 1]
    node: Node = Node(1, Node(2, Node(3, Node(3, Node(2, Node(1, None))))))
    assert print(linkify(int_list)) == print(node)


def test_scale_empty() -> None:
    """Scale should return None when given empty linked list."""
    assert scale(None, 2) == None


def test_scale_non_empty() -> None:
    """Scale should produce new linked list scaled by factor."""
    list_a = [3, 2, 1]
    answer = Node( 6, Node(4, Node(2, None)))
    assert print(scale(linkify(list_a), 2)) == print(answer)