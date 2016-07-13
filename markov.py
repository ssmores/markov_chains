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

    words = text_string.split()

    for i in (range(len(words) - 2)):
        two_words = (words[i], words[i+1])
        value = words[i+2]
        
        if chains.get(two_words): #this means that the key does exist
            
            chains.get(two_words).append(value) 
     
        else:
            chains[two_words] = [value]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # Select a random key from all the keys in the chains dictionary.
    first_key = choice(chains.keys())

    # Select a random value from key selected above.
    first_value = choice(chains[first_key])

    # This unpacks the key into individual identifiers, so we can add to the text.
    first_word, second_word = first_key

    # This updates the string with the identifies unpacked from the first key,
    # and adds them and the first value to the existing text string.
    text = "{} {} {} {}".format(text, first_word, second_word, first_value)

    # The next key is bound to the second word (of the original key), and the
    # value that was selected. 
    new_key = (second_word, first_value)


    # While the new key is in the keys in the dictionary
    while new_key in chains.keys():
        # Randomly select a value of the key from the chain dictionary
        # and bind that to a new value.
        new_value = choice(chains[new_key])
        # Unpack the list again, in order to eventually create new key.
        word1, word2 = new_key
        # Only adds the new value to the existing string.
        text = "{} {}".format(text, new_value)
        # Rebinds the key with the second word and new value.
        new_key = (word2, new_value)

    return text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
