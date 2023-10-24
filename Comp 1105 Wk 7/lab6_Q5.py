#function that gives true or false, true if a string has exactly 5 consecutive characters with the same value. 
#less or more than 5 consecutive characters is false.


#My function (broken)
def five_consecutive(string):
    #577777421 = True because 5 consecutive 7's
    #1827412 = False
    tracker = 1
    
    for n in range(1, len(string), 1):
        if str(n) == str(n - 1):
            tracker += 1
        else:
            if tracker == 5:
                return True
            tracker = 1
        if tracker == 5:
            return True
        return False


def main():
    checker = int(input("Enter a number: "))
    if five_consecutive(checker):
        print("There are 5 consecutive values")
    else:
        print("This string does not match the criteria")
    #print(check_five("55555312"))

five_consecutive(str(55555312))


#answer function 
#consecutive5 returns True or False
def consecutive5(str):
 count = 1 #counts the first character
 for i in range(1, len(str), 1):
    if str[i] == str[i-1] :
        count += 1
    else : #the sequence of equals ends
        if count == 5 :
            return True
        count = 1 #reset the counter and str[i] is the first
        #character in the row
        if count == 5 :
            return True
        return False
#Test your function
def main():
    num = input("Enter a string: ")
    if consecutive5(num) :
        print("The string has exactly-Five-consecutives")
    else :
        print("The string has no exactly-Five-consecutives")
#calling the main function
main()