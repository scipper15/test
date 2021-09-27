import sys

try:
    string_argument = sys.argv[1]

    # counts the number of words of a string passed in as a
    # command-line argument, excluding spaces and ignoring case
    print('Number of words (excluding spaces):', len(string_argument.split()))
except IndexError:
    print('Provide an argument please...')
