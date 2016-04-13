from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    f = open(file_path)
    text = f.read()
    f.close() 
    return text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    text = text_string.split()


    for i in range(len(text) -2):
        # if i + 1 < range(len(text) -1):
       
       #assign bi-gram tuples as dictionary keys
        chains[(text[i], text [i + 1])] = [] #<-- set value to list of  all words to right of tuple
    # Anything to the right of the existing keys inside the text will be set as an item in the value list


        # chains.get((text[i], text[i + 1]), 0)
        # else:
        #     return chains
    print chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
