import pathlib

NUM_ROWS = 10
NUM_COLS = 10
# return this tuple if a given word cannot be found
INVALID_WORD = (-1, -1)


def is_in_bounds(row: int, col: int) -> bool:
    """
    Check if a given row and column are within bounds.

    Inputs:

        row: int - row number
        col: int - column number

    Returns:

        True if row is in [0, NUM_ROWS) and col is in [0, NUM_COLS).
        (inclusive of 0, exclusive of upper bound).
        False otherwise.
    """
    # IMPLEMENTATION HERE


def check_word_direction(
    puzzle_grid: list[str],
    word: str,
    position: tuple[int, int],
    direction: tuple[int, int],
) -> bool:
    """
    Helper function to check if a given word is in a grid when following a given direction.

    Inputs:

        puzzle_grid: 2D grid of letters (all lower case)
        word: word to find
        position: (row, col) tuple
        direction: 2-int-tuple where each element is either -1, 0, or 1. Indicates direction.
            For example (0, 1) would mean searching along columns.
            (-1, 0) would indicate searching backwards along rows.

            For this assignment we will not use diagonal directions.
            (one of the two will always be 0)
    Returns:

        True if the word appears starting at the given position by incrementing
        the search in the given direction.
        False otherwise.
    """
    # IMPLEMENTATION HERE


def find_word(puzzle_grid: list[str], word: str) -> tuple[int, int]:
    """
    Find the first letter of a word, given a grid of letters and a word to find.

    See README for examples.

    Parameters:
        puzzle_grid: 2D grid of letters (all lower case)
        word: word to find

    Returns:
        Tuple of (row, column) indices of first letter of found word.

        If word could not be found, return INVALID_WORD constant defined above.
    """
    # IMPLEMENTATION HERE


def main():
    puzzle_path = pathlib.Path(__file__).parent / "puzzle.txt"
    # in practice, we should have error checking here but puzzle.txt is 10x10
    puzzle = puzzle_path.read_text().splitlines()

    words = ["python", "list", "tuple", "string", "int", "function", "float"]

    for word in words:
        position = find_word(puzzle, word)
        if position == INVALID_WORD:
            print(f"{word} not found")
        else:
            print(f"{word} found at {position}")


if __name__ == "__main__":
    main()
