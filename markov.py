from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    open_file = open(file_path)

    input_path = open_file.read()
    #print input_path

    return input_path


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi'): ['there']}
    """

    chains = {}
    new_value = []

    words = text_string.split()

    for i in (range(len(words) - 1)):
        two_words = (words[i], words[i+1])
        # print two_words

        if i < (len(words) - 2):
            new_value.append(chains.get(two_words, words[i + 2]))
            # new_value = chains.get(two_words, words[i+2])
            print new_value
            chains[two_words] = new_value

        # if i < (len(words) - 2):
            # chains = chains.get((words[i], words[i+1], following_word_values.append(words[i + 2])))
    # your code goes here

    # Pseudo code
    # Set the first tuple as a key
    # We need to map out the index of every word
    # So we can create a key, and then find the index of the next value to create the next key
    print chains
    return chains


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
