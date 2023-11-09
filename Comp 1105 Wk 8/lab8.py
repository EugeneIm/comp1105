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

def getStat(fileOne):
    file = open("one.txt", 'r')
    content = file.read()
    file.close("one.txt")
    dict = {}
    data = content.split()
    for data in data:
        data = data
        if data != None:
            dict[data] = dict.get(data, 0) + 1
    return data
 