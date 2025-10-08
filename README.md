# 51042 - Programming Assignment 1

## Goals

- Practice with types and control flow.
- Learn to read data from files.
- Implement a full program from scratch, going beyond just functions.

## General Reminders

### Helper Functions

You may implement any extra functions you deem necessary or useful. Remember to document them with docstrings.

### Keep Code in Functions

Unless you are defining a global variable that will remain constant, all code should be kept inside functions, on this and all future assignments.

### Style Guide

We expect you to follow the department [style guide](https://uchicago-cs.github.io/student-resource-guide/style-guide/python.html).

This is a significant portion of our grading, particularly on this assignment, refer to the [grading guide](https://mpcs51042.jpt.sh/coursework/programming/#code-quality-efficiency) for more details..

You may use a linter such as `ruff` to assist you, but be sure to follow documentation and variable naming rules, which linters typically cannot help with.

### Running `pytest`

Each problem comes with some helpful tests.
These are not guaranteed to be comprehensive, it may benefit you to consider other cases as well.

You can run `uv run pytest` from this directory to run all tests for the homework.

To just run a subset of tests, you can specify the directory name, e.g. `uv run pytest collatz`.

See [pytest tips on the course site](https://mpcs51042.jpt.sh/coursework/programming/#pytest-tips) for helpful tips.

## Problems

### Part 1 - Word Search

Word search puzzles consist of a grid of letters, and a set of words to find, for example:

```
xyzcw
pmnam
abctw
frogo
cvbnc
```

Contains:

- cat starting at (row=0, column=3) & heading down
- frog starting at (3, 0) & heading right
- cow starting at (4, 4) & heading up
- man starting at (1, 4) & heading left

`wordsearch.py` contains the beginnings of a program to solve these puzzles.

You will implement three functions:

- `is_in_bounds` - determine if coordinates are within bounds.
- `check_word_direction` - a helper function that will return True or false if a word is at a particular location.
- `find_word` - which will take a puzzle and word and return the position of the first letter.

Each of these functions has separate tests.
You will complete them one at at time, in the given order.

It will be helpful to run the tests as you work,
so that you can verify that each function works as expected before moving on to the next.

Open `wordsearch/wordsearch.py` and implement the functions within.

Once all tests are passing, you should also be able to run the program's `main` function which will solve a puzzle in puzzle.txt.

#### Note About Types

Pay close attention to types given in the problem. Doing so will help avoid the most common errors.

Also, you may wonder why we use a `list[str]` instead of a `list[list[str]` here as we've seen with other grids.

Since we aren't modifying the grid at all and `list` and `str` are both **sequence types**, having our data resemble:

```python
[
  "xyzcw",
  "pmnam",
  "abctw",
  "frogo",
  "cvbnc",
 ]
```

Works just as well as the more complicated list-of-lists. We can still access individual letters as `grid[row][col]`.

### Part 2 - Chicago Towing

For this problem, we're going to deal with some real world data.

`towing/towing.csv` is a comma separated value (CSV) file [downloaded from the City of Chicago](https://data.cityofchicago.org/Transportation/Towed-Vehicles/ygr5-vcbg) with real world data on vehicles towed in a 90 day period.

**Note**: See [Files](https://dir-python.jpt.sh/files/) for details on how to read from files. You'll want to use `pathlib` and `csv`.

It may be helpful to look at [csv.DictReader](https://docs.python.org/3/library/csv.html) examples.

We are going to implement two functions to generate reports from this data.

`top_days(n)` should return an ordered list of the top `n` days of towing.

Each item in the list should be a tuple of the date and the number of vehicles towed.

So `top_days(3)` might return:

```python
[
  ("09/17/2022", 128),
  ("09/28/2022", 116),
  ("09/24/2022", 94),
]
```

And `day_summary` should return a similar list-of-tuples, except the ordering should be by date.

```python
[
  ("07/01/2022", 5),
  ("07/02/2022", 5),
  ... # truncated
  ("09/29/2022", 94),
]
```

Open `towing/towing.py` & implement `top_days` and `day_summary`.

Tip #1: You may want to implement other helper functions, as always, you are free to do so however you wish.

Tip #2: You will want to convert dates from strings to the `datetime` type for the purposes of comparison.

`datetime.strptime` Example:

```python
import datetime

date_str = "06/15/2022"
date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
```

### Part 3 - Word Counting

For this assignment you will not be given a pre-written set of functions.
Instead, you are going to write a program from scratch.

Your program should take a list of files from the command line, so that if one were to run:

```
$ uv run python3 summarize.py file1.txt file2.txt
file1.txt: 26 words, 10 unique
file2.txt: 10 words, 1 unique
total: 36 words, 10 unique
```

That is, for each file print a line for each file containing:

- the name of the file
- the count of total words as well as unique words in the file after:
  - replacing punctuation characters with spaces (Use [`string.punctuation`](https://docs.python.org/3/library/string.html#string.punctuation) to match expected output.)
  - splitting on whitespace
  - converting all text to lower case

And a final line that contains:

- 'total' where the filename would be
- the total number of words across all files
- the total number of unique words **across all files** not counting duplicates between files. This is **NOT** the sum of the unique words in each file. See Example 3 below to clarify.

#### Testing

Since we have not chosen functions for you, we cannot provide specific tests.

Instead, we have provided some files you can test with. You can test with a subset, or with all at once:

```
$ cd summarize/  # it will be easier to run this from within the summarize [directory](directory.md)
$ uv run python3 summarize.py buffalo.txt long.txt one.txt punctuation.txt
buffalo.txt: 8 words, 1 unique
long.txt: 338 words, 13 unique
one.txt: 9 words, 9 unique
punctuation.txt: 24 words, 4 unique
total: 379 words, 21 unique
```

If you'd like to attempt writing your own tests for smaller functions, looking at tests in this assignment and the previous may be helpful, but is not required.

#### Example 1 - Normalization

"This this this." -> 3 words, 1 unique

Punctuation and then lower-casing leads to "this this this" as the final string.

#### Example 2 - Punctuation

"u.s.a." -> 3 words, 3 unique

This happens because the punctuation split must happen first, creating "u s a". This will also happen with other characters like apostrophes and hyphens.

#### Example 3 - Total Unique

This relates to how the total unique count must work.
Consider two files:

a.txt

```
apple banana
```

b.txt

```
apple apple apple
```

The expected output would be:

```
a.txt: 2 words, 2 unique
b.txt: 3 words, 1 unique
total: 5 words, **2 unique**
```

On the final line, the 5 is computed by simply adding the total words in each file, `3 + 2 = 5`.

The 2 however, requires a more complex solution, since simply adding `1 + 2 = 3` would be incorrect, since the only two unique words are apple and banana.
