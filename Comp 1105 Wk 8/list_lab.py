#Short answer
#Q1. 
mystr = 'yes'
mystr += 'no'
mystr -= 'yes'
print(mystr)
#This will give you "yesnoyes"

#Q2
mystr = 'abc' * 3
#This will give you an error because you are trying to multiply a str with an int. 
print(mystr)

#Q3
mystr = 'abcedfg'
print(mystr[2:5])
#This prints only the section where the index starts at 2 and ends at 5
    #It will give you 'cdef'

#Q4
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[4:6])
#Again, this will only print from index 4 to index 6
    #567

#Q5
name = 'joe'
print(name.lower())
    #joe
print(name.upper())
    #JOE
print(name)
    #joe


def updateOne(str):
    str = str + 'value'
    print('in update 1', str)
def updateTwo(ls):
    ls[1] == 15
    print("in update 2", ls)
word = 'new values'
data = [100, 200, 300]
updateOne(word)
updateTwo(data)

print(word, data)