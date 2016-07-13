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

    first_key = choice(chains.keys())
    first_value = choice(chains[first_key])
    first_word, second_word = first_key
    text = "{} {} {} {}".format(text, first_word, second_word, first_value)
    new_key = chains.get((second_word, first_value), 0)

    # we need to make 'you' the first part of the tuple key
    # we need to make 'could' the second part of the tuple key  

    # first_key = ('would', 'you')
    # first_word = 'would'
    # second_work = 'you'
    # first_value = 'could' randomly selected
    # new_key = ('you', 'could')


    while new_key != 0:
        new_value = choice(chains[new_key])
        # new_value = 'I'
        text = "{} {}".format(text, new_value)
        # "would you could I"
        new_value = chains.get((first_value, new_value), 0)
        # new_value = chains.get(('you', 'could'), 0)
        # we need ('could', 'I') instead of the ('you', 'could')







    # We need an if statement for if the "new key" is not a key in the dictionary, then we stop. 
    # We need a condition for the while loop such that it will continue if the key exists in the dictionary.
    
    print text

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
