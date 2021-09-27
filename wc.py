import sys

try:
    string_argument = sys.argv[1]

    # counts the number of words of a string passed in as a
    # command-line argument, excluding spaces and ignoring case

    # adding a new function, which also counts the numbers of
    # chars

    # allow for directory-names as input arguments - in this case,
    # the word count is to be applied to all text-files of that directory
    print('Number of words (excluding spaces):', len(string_argument.split()))
    print('Number of chars (including spaces):', len(string_argument))
except IndexError:
    print('Provide an argument please...')
