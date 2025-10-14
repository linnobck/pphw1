"""
Usage:
$ python3 summarize.py <file1> <file2> [... <fileN>]
file1: 30 words, 12 unique
file2: 10 words, 1 unique
total: 40 words, 12 unique
"""

import sys, string
from pathlib import Path

# this was for testing my output
#BASE_DIR = Path(__file__).parent
#data_path = BASE_DIR / "one.txt"
#data_path2 = BASE_DIR / "long.txt"

def summarize(files: list) -> str:
    """
    Input:
        Take a list of files from the command line.
 
    This function computes a file's total number of words, and its unique words.
        
    Output:
        String for each file containg the file name,
        The total number of words across all files, and unique words,
        The total number of unique words across all files.
    
    """
    # initialize empty set, total word count
    total_unique_words = set()
    total_word_count = 0
    results = []

    # loop through all files
    for file in files:
        # store stats for each file
        file_name = ""
        file_words = 0
        file_unique = set()
        
        # turn each line into individual word strings
        with open(file, "r") as f:
            #file_name = os.path.basename(file)
            for line in f:
                line = line.lower().strip()
                # use .maketrans() to delete all punctuation and replace w space
                line = line.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
                words = line.split()
                # add num of words to file word count and total word count
                file_words += len(words)
                total_word_count += len(words)
                # add word to file unique words, they will be unique becuase of the set() functionality
                file_unique.update(words)
                # add word to total unique words, they will be unique becuase of the set() functionality
                total_unique_words.update(words)
            # append formatted result strings to list
            results.append(f"{file}: {file_words} words, {len(file_unique)} unique")
    results.append(f"total: {total_word_count} words, {len(total_unique_words)} unique")

    #return formatted results
    return "\n".join(results)


def main():
    # sys.argv is a list of strings
    # sys.argv[0] is always the name of the program, so we typically skip it
    # sys.argv[1:] are the arguments passed on the command line
    #
    # Suppose we run `python3 example.py a b c` in the terminal,
    # then sys.argv = ["a", "b", "c"]
    #
    # Get list of files from command line
    files = sys.argv[1:]

    # check for at least one file
    if not files:
        sys.exit(1)

    # call summarize() with provided file/s
    summary = summarize(files)
    print(summary)


if __name__ == "__main__":
    main()
