"""
Usage:
$ python3 summarize.py <file1> <file2> [... <fileN>]
file1: 30 words, 12 unique
file2: 10 words, 1 unique
total: 40 words, 12 unique
"""

import sys


def main():
    # sys.argv is a list of strings
    # sys.argv[0] is always the name of the program, so we typically skip it
    # sys.argv[1:] are the arguments passed on the command line
    #
    # Suppose we run `python3 example.py a b c` in the terminal,
    # then sys.argv = ["a", "b", "c"]
    #
    # TODO: delete this one line below once you add your implementation
    print("sys.argv =", sys.argv[1:])

    # COMPLETE THIS FUNCTION


if __name__ == "__main__":
    main()
