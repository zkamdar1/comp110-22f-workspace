"""Testing our functions from utils."""

__author__ = "730476042"


from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Test only_evens function with empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_one_item() -> None:
    """Test only_evens function with one item in list."""
    x: list[int] = [1]
    assert only_evens(x) == []


def test_only_evens_many_items() -> None:
    """Test only_evens function with list."""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(x) == [2, 4, 6]


def test_concat_empty_lists() -> None:
    """Test concat function with empty lists."""
    xa: list[int] = []
    xb: list[int] = []
    assert concat(xa, xb) == []


def test_concat_one_empty_list() -> None:
    """Test concat function with one empty list."""
    xa: list[int] = [1, 2, 3]
    xb: list[int] = []
    assert concat(xa, xb) == [1, 2, 3]


def test_concat_no_empty_lists() -> None:
    """Test concat function with no empty list."""
    xa: list[int] = [2, 4, 6]
    xb: list[int] = [1, 3, 5]
    assert concat(xa, xb) == [2, 4, 6, 1, 3, 5]


def test_sub_empty_list() -> None:
    """Test sub function with empty list."""
    za: list[int] = []
    start: int = 1
    end: int = 2
    assert sub(za, start, end) == []


def test_sub_normal_list() -> None:
    """Test sub function with list."""
    za: list[int] = [10, 20, 30, 40, 50, 60]
    start: int = 1
    end: int = 4
    assert sub(za, start, end) == [20, 30, 40]


def test_sub_negative_start() -> None:
    """Test sub function with negative start value."""
    za: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = -1
    end: int = 3
    assert sub(za, start, end) == [1, 2, 3]


def test_sub_greater_end() -> None:
    """Test sub function with end value greater than len of list."""
    za: list[int] = [2, 4, 6, 8, 10, 12, 14]
    start: int = 2
    end: int = 8
    assert sub(za, start, end) == [6, 8, 10, 12, 14]
