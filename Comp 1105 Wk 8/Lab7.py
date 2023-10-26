# Write a modular program that receives data from a file called 'data.txt' and prints out the contents
# Try except functions

# ZeroDivisionError
# FileNotFoundError
try:
    print(5/0)
except ZeroDivisionError:
    print("cannot divide by 0")

print("Give me two numbers and i'll divide them")
print('enter q to quit any time')
while True:
    num_one = input("\n First Number: ")
    if num_one == "q":
        break
    num_two = input("\n Second Number: ")
    if num_two == "q":
        break
    try:
        answer = int(num_one)/int(num_two)
    except ZeroDivisionError:
        print("Cannot divide by 0")
    else:
        print(answer)

#Reading the file
try:
    file_read = open("data.txt", "r")
    #r is read, w is write, a is append
    data = file_read.read()
    #.read(), .write(), .append()
    print(data)

    file_read.close()
    #close the file
except FileNotFoundError:
    print("File is not found")

#While loop to read a file
try:
    file_content = open('data.txt', 'r')
    while True:
        line = file_content.readline()
        if line == '':
            break
    file_content.close()
except FileNotFoundError:
    print("File not found")

#Writing to a file
try:
    content = open('out.txt', 'w')
    file_content = ("This writes to a file")
    info = content.write(file_content)
    print(info)
    content.close()
except FileNotFoundError:
    print("file not found")


#Calculate the average while reading the file
'''
1. Read the contents of the file
2. Store the numbers into a variable
3. Count how many values were read
4. Divide the variable by the amount of lines

'''

def main():
    try:
        numbers = open('data.txt', 'r')
        total = 0
        count = 0
        while True:
            line = numbers.readline()
            if line == '':
                break
            count += 1
            num = float(line)
            total += num
        print("The average in data.txt is:", total/count)
        numbers.close()
    except FileNotFoundError:
        print("file not found")
        return
    except ValueError as verr:
        print("MyError : ", verr)

main()