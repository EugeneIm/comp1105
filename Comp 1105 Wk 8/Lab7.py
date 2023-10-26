# Write a modular program that receives data from a file called 'data.txt' and prints out the contents
# Try except functions

# ZeroDivisionError
# FileNotFoundError
#
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

file = "two.txt"

