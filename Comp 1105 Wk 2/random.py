x = input("Enter a number ")
x = float(x)
y = input("Enter another number ")
y = int(y)
z = input("What's your name: ")
z = str(z)

NAME = "name"

print(format(x, '20.2f'))
print(format(y, '20'))
print(format(x + y, '20.2f'))

print(format(NAME, '>25'), format(NAME, '<25'), sep="@")
print(format(x, '>25'), format(y, '<25'), sep="@")



a = True #bool data type
print(type(a))
print(type('a'))

