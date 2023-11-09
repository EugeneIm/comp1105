#Q1 Function named "count", given a list of words, returns a dictionary of the words and how many times they have been repeated.
    #i.e. ["is", 'is", 'this", "this"]
    #returns a dictionary {"is":2, "this":2}
list_words = ["is", "the", "season", "The", "computer", "the", "Is", "COMPUTER"]

def count_words(ls):
    dict = {}
    for word in ls:
        word = word.title()
        dict[word] = dict.get(word, 0) + 1
    return dict
full_dict = count_words(list_words)
print(full_dict)


#Q2 function called getStat(), given a file name, returns a dictionary of the words and numbers and their occurence in the file. 
    #Function is case sensitive (use either .lower(), .upper(), .title())

def getStat():
    file = open("one.txt", 'r')
    content = file.read()
    file.close()
    dictionary = {}
    data = content.split()
    for data in data:
        data = data
        if data != None:
            dictionary[data] = dictionary.get(data, 0) + 1
    return dictionary
full_dictionary = getStat()
print(full_dictionary)


#Q3 use the function from Q2 and read the contents of 2 files and compare them to do the following:
    #create a function named uniqueWords() where it returns a list of all words that were listed only once
    #function called moreThanOnce() where it returns a list of words listed more than once
    #function called onlyInFirst(), returns the words in the first list and not the second
    #function called moreThanTwice(), returns words that were listed more than twice 
    #main function to call all the above functions 

def getStat():
    file = open("one.txt", 'r')
    content = file.read()
    file.close()
    dictionary = {}
    data = content.split()
    for data in data:
        data = data
        if data != None:
            dictionary[data] = dictionary.get(data, 0) + 1
    return dictionary
full_dictionary = getStat()
print(full_dictionary)