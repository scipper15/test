import sys

try:
    string_argument = sys.argv[1]

    print('Number of words (excluding spaces):', len(string_argument.split()))
except IndexError:
    print('Provide an argument please...')
