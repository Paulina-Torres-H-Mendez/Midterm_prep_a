# Write a function that takes the name of a text file as parameter. Print out the 3-
# letter words that start with “b”
punctuation = ",.!?"
def find_words(filename):
    """prints the 3 letter word starting with b
    :param filename:the name of the file
    :return: Nothing
    """
    with open(filename, 'r') as f:
        for line in f:
            for p in punctuation:
                line = line.replace(p," ")
            # need to break down the line into words
            words = line.split() # by default splits by space
            #check each word
            for word in words:
                if len(word) ==3 and word.upper()[0] == "B":
                    print(word)

find_words("input.txt")


