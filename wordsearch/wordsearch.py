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

    if row not in range(0,NUM_ROWS) or col not in range(0,NUM_COLS):
        return False
    else:
        return True


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

    # create variables out of the inputs to navigate grid
    starting_row = position[0]
    starting_col = position[1]
    
    direction_row = direction[0]  # change in row per step
    direction_col = direction[1]  # change in col per step 
    
    word_length = len(word)

    i = 0 # keep track of steps in grid

    while i < word_length:
        new_row = starting_row + (i * direction_row)
        new_col = starting_col + (i * direction_col)

        # if steps go out of bounds
        if not is_in_bounds(new_row, new_col):
            return False

        # compare if grid letter and letter in word are equal      
        position_letter = puzzle_grid[new_row][new_col]
        word_letter = word[i]

        if position_letter != word_letter:
            return False
        
        # increment count and go to the next letter
        i += 1

    return True



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
    directions = [(1,0), (-1,0), (0,1), (0,-1)]


    # go through letters in grid
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            current_letter = puzzle_grid[i][j]
            
            # start search into diff directions if grid letter is the same as first letter in word
            if current_letter == word[0]:
                for d in directions:
                    success = check_word_direction(puzzle_grid, word, (i,j), d)
                    if success:
                        return (i,j)
                    
    return INVALID_WORD






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
