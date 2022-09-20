"""Examples of importing Python."""


from lessons import helpers
# Alias a module / imported as another name
from lessons import helpers as hp

# Imports names defines globally in a module
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {helpers.THE_ANSWER}")


    if __name__ == "__main__":
        main()