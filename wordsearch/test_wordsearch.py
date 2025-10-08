import pytest
from wordsearch import check_word_direction, is_in_bounds, find_word


# This is a shortcut for writing lots of very similar tests.
# If you'd like to better understand take a look at
# https://docs.pytest.org/en/7.1.x/how-to/parametrize.html
#
# Each 3-tuple below is a set of 2 parameters and an expected value.
@pytest.mark.parametrize(
    "r,c,expected",
    [
        (0, 0, True),
        (5, 5, True),
        (-1, 0, False),
        (3, -1, False),
        (100, 100, False),
        (9, 10, False),
        (10, 9, False),
        (9, 9, True),
    ],
)
def test_in_bounds_p(r, c, expected):
    assert is_in_bounds(r, c) is expected


# puzzle from README padded out to 10x10
example_puzzle = [
    "xyzcw00000",
    "pmnam00000",
    "abctw00000",
    "frogo00000",
    "cobnc00000",
    "0000000000",
    "0000000000",
    "0000000000",
    "00g0000000",
    "fro0000000",
]

cat_pos = (0, 3)  # down
frog_pos = (3, 0)  # right
man_pos = (1, 4)  # left
cow_pos = (4, 4)  # up


def test_check_word_direction_down():
    assert check_word_direction(example_puzzle, "cat", cat_pos, (1, 0))


def test_check_word_direction_right():
    assert check_word_direction(example_puzzle, "frog", frog_pos, (0, 1))


def test_check_word_direction_left():
    assert check_word_direction(example_puzzle, "man", man_pos, (0, -1))


def test_check_word_direction_up():
    assert check_word_direction(example_puzzle, "cow", cow_pos, (-1, 0))


def test_word_wrong_dir():
    # right starting letter, wrong direction
    assert check_word_direction(example_puzzle, "cow", cow_pos, (0, -1)) is False
    assert check_word_direction(example_puzzle, "man", man_pos, (1, 0)) is False


def test_word_no_turns():
    # the first 3 letters appear, but the 'g' would require a turn
    assert check_word_direction(example_puzzle, "frog", (9, 0), (0, 1)) is False


def test_find_word_good():
    assert find_word(example_puzzle, "cat") == cat_pos
    assert find_word(example_puzzle, "frog") == frog_pos
    assert find_word(example_puzzle, "man") == man_pos
    assert find_word(example_puzzle, "cow") == cow_pos


def test_find_word_missing():
    assert find_word(example_puzzle, "octopus") == (-1, -1)
