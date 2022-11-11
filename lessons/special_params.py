"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: Union[str, int] = "World") -> str:
    """A fun greeting."""
    greeting: str = "hello, "
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else:
        greeting += "Alien Life from sector " + str(name)
    return greeting

# one arguement:
print(hello("sally"))

# No arguments:
print(hello())

# int arguement works too
print(hello(110))