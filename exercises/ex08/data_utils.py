"""Dictionary related utility functions."""

__author__ = "730476042"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row__table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row__table[0]
    for column in first_row:
        result[column] = column_values(row__table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with specific amount of rows."""
    result: dict[str, list[str]] = {}
    
    for key in table:
        values: list[str] = []
        i: int = 0
        while i < rows:
            if rows >= len(table):
                return table
            else:
                key_value = list(table[key])
                values.append(key_value[i])
                i += 1
        result[key] = values
    return result


def select(main: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with specific columns."""
    result: dict[str, list[str]] = {}

    for key in names:
        result[key] = main[key]

    return result


def concat(table_a: dict[str, list[str]], table_b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Given two column-based tables, produces a combined table."""
    result: dict[str, list[str]] = {}

    for key in table_a:
        result[key] = table_a[key]

    for items in table_b:
        present: bool = items in result
        if present is True:
            result[items] += table_b[items]
        else:
            result[items] = table_b[items]
    return result


def count(data: list[str]) -> dict[str, int]:
    """Returns a dict of the frequencies of items in list."""
    result: dict[str, int] = {}

    for item in data:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
