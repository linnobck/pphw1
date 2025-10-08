# Note: since we do not define the function decomposition we cannot provide detailed tests.
#
# It may be benefical to write some small tests of your own. Refer to tests in earlier problems
# for ideas.

import sys
from summarize import main


def test_main(capsys):
    # this is the test that runs on gradescope
    # it needs to use some less-common features since we are testing the
    # output of print statements
    #
    # typically your tests shouldn't do this, instead testing return values
    # of smaller functions instead
    #
    # note: to pass, this test needs to be run from outside the 'summarize/' directory
    sys.argv = [
        ".",
        "summarize/buffalo.txt",
        "summarize/long.txt",
        "summarize/one.txt",
        "summarize/punctuation.txt",
    ]
    main()
    output = capsys.readouterr()
    expected = """summarize/buffalo.txt: 8 words, 1 unique
summarize/long.txt: 338 words, 13 unique
summarize/one.txt: 9 words, 9 unique
summarize/punctuation.txt: 24 words, 4 unique
total: 379 words, 21 unique
"""
    assert output.out == expected
