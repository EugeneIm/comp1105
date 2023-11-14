#Review Q1
#Write a program that returns a person's initials, i.e. John Willian Smith -> J W S

#Q1
def get_initials():
    #user inputs their name
    name = getName()
    result = getInitials(name)
    print(result)

def getName():
    full_name = input("Full government name please: ")
    return full_name

def getInitials(name):
    list = name.split()
    initials = ""
    #Below is a for loop that iterates over every item in your set. 
    for l in list:
        initials += l[0].upper() + ". "
    return initials
    
get_initials()


#Encrypt a dictionary to a file
def main():
    filename = input('Enter the filename please ')
    codes = {'A':'%', 'a':'9', 'B':'@', 'b':'*'}
    content = getData(filename)
    result = encrypt(codes, content)
    #writing to a file
    outFileName = input('Enter a file name to write to: ')
    outPut('out.txt', result)
    print(content)
    print(result)

def getData(fname):
    #infinite loop so that if you put in an invalid file name, it lets you try it again. 
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
        #for each of the keys in the key value pairs, use the replace method to reverse the key's and values to encrypt it. 
        text = text.replace(key, d[key])
    return text

main()

#Q2 Date printer

#Input = 03/12/2023, Output is March 12, 2023
