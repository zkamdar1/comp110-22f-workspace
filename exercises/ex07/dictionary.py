"""Ex-06 - Practice with dictionary functions."""

__author__ = "730476042"


def invert(book: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, returns dictionary with inverted keys and values."""
    result: dict[str, str] = {}
    for key in book:
        if book[key] in result:
            raise KeyError("Duplicate keys")
        result[book[key]] = key

    return result


def count(items: list[str]) -> dict[str, int]:
    """Given a list, will output a dictionary where key is unique value in list and value is the number of times it appears in list."""
    new_dict: dict[str, int] = {}
    
    for key in items:
        if key in new_dict:
            new_dict[key] += 1
        else:
            new_dict[key] = 1

    return new_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Given a dictionary of names and favorite colors, returns a str of most common color."""
    color_list = list(colors.values())
    result: str = ""
    tracker: dict[str, int] = {}
    tracker = count(color_list)

    max_value: int = 0
    for k, v in tracker.items():
        if v >= max_value:
            if v > max_value:
                max_value = v
                result = k
            else:
                result = color_list[0]

    return result