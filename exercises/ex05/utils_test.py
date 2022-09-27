"""Testing our functions from utils."""

__author__ = "730476042"

from utils import only_evens

def test_only_evens_empty() -> None:
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_one_item() -> None:
    x: list[int] = [1]
    assert only_evens(x) == []


def test_only_evens_many_items() -> None:
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(x) == [2, 4, 6]


from utils import concat

def test_concat_empty_lists() -> None:
    xa: list[int] = []
    xb: list[int] = []
    assert concat(xa, xb) == []

def test_concat_one_empty_list() -> None:
    xa: list[int] = [1, 2, 3]
    xb: list[int] = []
    assert concat(xa, xb) == [1, 2, 3]

def test_concat_no_empty_lists() -> None:
    xa: list[int] = [2, 4, 6]
    xb: list[int] = [1, 3, 5]
    assert concat(xa, xb) == [2, 4, 6, 1, 3, 5]


from utils import sub

def test_sub_empty_list() -> None:
    za: list[int] = []
    start: int = 1
    end: int = 2
    assert sub(za, start, end) == []

def test_sub_normal_list() -> None:
    za: list[int] = [10, 20, 30, 40, 50, 60]
    start: int = 1
    end: int = 4
    assert sub(za, start, end) == [20, 30, 40]

def test_sub_negative_start() -> None:
    za: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = -1
    end: int = 3
    assert sub(za, start, end) == [1, 2, 3]

def test_sub_greater_end() -> None:
    za: list[int] = [2, 4, 6, 8, 10, 12, 14]
    start: int = 2
    end: int = 8
    assert sub(za, start, end) == [6, 8, 10, 12, 14]
