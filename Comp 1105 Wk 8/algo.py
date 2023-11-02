#Determine if the choice is equal to 'Y' or 'y'

while True: 
    letter = input('give me a letter ')
    target = "Y"
    quit = "quit"
    if letter == target.upper():
        print("You got the target letter")
        break
    elif letter == "quit":
        print("type 'quit' if you want to stop")
        break
    else:
        print("The letter is wrong")


#Write a loop that counts the number of space characters that appear in the string referenced by mystring

def check_space(string):
    count = 0
    for x in string:
        if x == " ":
            count += 1
    return count

string = "Welcome to geeksforgeeks, Geeks!"
print("num whitespaces = ",check_space(string))
#print(mystring.count(" "))
#Keep returning 0 for some reason

#Write a loop that counts the number of digits in "mystring"
