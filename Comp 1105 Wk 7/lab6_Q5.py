#function that gives true or false, true if a string has exactly 5 consecutive characters with the same value. 
#less or more than 5 consecutive characters is false.



def five_consecutive(string):
    #577777421 = True because 5 consecutive 7's
    #1827412 = False
    tracker = 1
    
    for n in range(1, len(tracker), 1):
        if str(n) == str(n - 1):
            tracker += 1
        else:
            if tracker == 5:
                return True
            tracker = 1
            


    #print(check_five("55555312"))

five_consecutive(str(55555312))