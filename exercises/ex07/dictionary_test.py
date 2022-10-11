"""Tests for practice dictionary functions."""

__author__ = "730476042"


def test_invert_empty() -> None:
    """Test only_evens function with empty list."""
    x: list[int] = []
    assert invert(x) == []


def test_invert_one_item() -> None:
    """Test only_evens function with one item in list."""
    x: list[int] = [1]
    assert invert(x) == []


def test_invert_many_items() -> None:
    """Test only_evens function with list."""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert invert(x) == [2, 4, 6]



def test_favorite_color_empty() -> None:
    """Test only_evens function with empty list."""
    x: list[int] = []
    assert favorite_color(x) == []


def test_favorite_color_one_item() -> None:
    """Test only_evens function with one item in list."""
    x: list[int] = [1]
    assert favorite_color(x) == []


def test_favorite_color_many_items() -> None:
    """Test only_evens function with list."""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert favorite_color(x) == [2, 4, 6]



def test_count_empty() -> None:
    """Test only_evens function with empty list."""
    x: list[int] = []
    assert count(x) == []


def test_count_one_item() -> None:
    """Test only_evens function with one item in list."""
    x: list[int] = [1]
    assert count(x) == []


def test_count_many_items() -> None:
    """Test only_evens function with list."""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert count(x) == [2, 4, 6]