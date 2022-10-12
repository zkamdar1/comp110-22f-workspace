"""Tests for practice dictionary functions."""

__author__ = "730476042"

from dictionary import invert, count, favorite_color

def test_invert_empty() -> None:
    """Test invert function with empty dictionary."""
    x: dict[str, str] = {}
    assert invert(x) == {}


def test_invert_one_item() -> None:
    """Test invert function with one key and value."""
    x: dict[str, str] = {'a': '1'}
    assert invert(x) == {'1': 'a'}


def test_invert_many_items() -> None:
    """Test invert function with multiple keys and values."""
    x: dict[str, str] = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
    assert invert(x) == {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}



def test_favorite_color_empty() -> None:
    """Test favorite_color function with empty dictionary."""
    x: dict[str, str] = {}
    assert favorite_color(x) == ''


def test_favorite_color_one_item() -> None:
    """Test favorite_color function with two same colors in list."""
    x: dict[str, str] = {'Zaid': 'red', 'Bob': 'red', 'Jim': 'red', 'Carl': 'blue'}
    assert favorite_color(x) == 'red'


def test_favorite_color_many_items() -> None:
    """Test favorite_color function with equal amounts of colors."""
    x: dict[str, str] = {'Zaid': 'blue', 'Bob': 'red', 'Jim': 'purple', 'Carl': 'yellow'}
    assert favorite_color(x) == 'blue'



def test_count_empty() -> None:
    """Test count function with empty list."""
    x: list[str] = []
    assert count(x) == {}


def test_count_one_item() -> None:
    """Test count function with same items in list."""
    x: list[str] = ['a', 'b', 'a', 'a', 'c']
    assert count(x) == {'a': 3, 'b': 1, 'c': 1}


def test_count_many_items() -> None:
    """Test count function with different items in list."""
    x: list[str] = ['a', 'b', 'c']
    assert count(x) == {'a': 1, 'b': 1, 'c': 1}