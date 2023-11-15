# Review Q1
# Write a program that returns a person's initials, i.e. John Willian Smith -> J W S
# Q1
'''
def get_initials():
    # user inputs their name
    name = getName()
    result = getInitials(name)
    print(result)


def getName():
    full_name = input("Full government name please: ")
    return full_name


def getInitials(name):
    list = name.split()
    initials = ""
    # Below is a for loop that iterates over every item in your set.
    for l in list:
        initials += l[0].upper() + ". "
    return initials


get_initials()
'''
'''

# Encrypt a dictionary to a file
def main():
    filename = input('Enter the filename please ')
    codes = {'A': '%', 'a': '9', 'B': '@', 'b': '*'}
    content = getData(filename)
    result = encrypt(codes, content)
    # writing to a file
    outFileName = input('Enter a file name to write to: ')
    outPut('out.txt', result)
    print(content)
    print(result)


def getData(fname):
    # infinite loop so that if you put in an invalid file name, it lets you try it again.
    while True:
        try:
            file = open(fname, 'r')
            contents = file.read()
            file.close()
            return contents
        except Exception as err:
            print("Error: ", err)
            fname = input('enter the file name please: ')


def outPut(fname, message):
    file = open(fname, 'w')
    file.write(message)
    file.close()


def encrypt(d, text):
    for key in d:
        # for each of the keys in the key value pairs, use the replace method to reverse the key's and values to encrypt it.
        text = text.replace(key, d[key])
        # Replacing the key:value pair to be value:key, therefore encrypting the text.
    return text


main()

'''
# Q2 Date printer

# Input = 03/12/2023, Output is March 12, 2023


def dateChange():
    # Get the input from the user
    formatOne = input('Enter the date in the format: XX/XX/XXXX please: ')
    d = {1: 'Jan', 2: 'Feb', 3: 'March'}
    result = convertDate(formatOne, d)
    if result != None:
        print(result)


def convertDate(date, d):
    try:
        ls = date.split('/')
        result = d[int(ls[0])] + ' ' + str(int(ls[1])) + ', ' + str(int(ls[2]))
        return result
    except ValueError as err:
        print('Error: ', err)
        return None


dateChange()


letters = set()
with open('test.txt') as content:
    upper = 0
    lower = 0
    digits = 0
    spaces = 0

    text = content.read()
    for char in text:
        if char.isupper():
            upper += 1
            letters.add(char)
        elif char.islower():
            lower += 1
            letters.add(char)
        elif char == " ":
            spaces += 1
            letters.add(char)
        elif char.isdigit() == True:
            digits += 1
            letters.add(char)
    print("Number of upper case letters:", upper,
          "\nNumber of lower case letters:", lower, "\nNumber of spaces:", spaces, "\nNumber of digits:", digits)
