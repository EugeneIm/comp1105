#1 byte is 8 bits
#1 kb(kilobyte) is 1024 bytes
#1 MB is 1,048,576 bytes
#1 GB is 1,073,741,824 bytes
IDE = ['Sublime', 'PyCharm', 'Wing', 'GUI']
IDE.append("VSCode")
print(IDE);
#Above is just a list of IDE's made for fun


"Question 1"
#Convert the following numbers to decimals and show your work. 
#Binary column values (2^6)(2^5)(2^4)(2^3)(2^2)(2^0)
#1. 1101(2)
'''
1's are positioned at the ^0, ^2, ^3 = 1 + 4 + 8
8+4+0+1 = 13
'''
#2. 10101010(2)
'''
1's are positioned at the ^1, ^3, ^5, ^7 = 2 + 8 + 32 + 128
2+8+32+128 = 170
'''

"Question 2"
#Convert the decimals numbers 457 and 988 to the binary. You are supposed to use the algorithm for converting decimal to binary.
'''
457 => 100101110
457/2 = 228 + 1
228/2 = 114 + 0
114/2 = 57 + 0
57/2 = 28 + 1
28/2 = 14 + 0
14/2 = 7 + 1
7/2 = 3 + 1
3/2 = 1 + 1
1/2 = 0
'''
'''
988 => 1111011100
988/2 = 494 + 0
494/2 = 247 + 0
247/2 = 123 + 1
123/2 = 61 + 1
61/2 = 30 + 1
30/2 = 15 + 0
15/2 = 7 + 1
7/2 = 3 + 1
3/2 = 1 + 1
1/2 = 0 + 1
'''

"Question 3"
#Consider that we only have 1 byte to remember data (1 byte is 8 bits).
#How many numbers can be represented?
"With only 1 byte, you can represent 256 numbers because it is (2^8)"
#How many numbers can be represented if we have N bytes rather than 1 byte?
"With any amount of bytes it is just (2^n). i.e. 2 bytes can represent (2^16) = 65,536 different values. 3 bytes would just be (2^24) amount of values."

"Question 4"
#Use the ASCII encoding table to represent the following characters or strings in binary.
#1. 124 on the ASCII encoding table
"Column 9 Row #4, Column 0 Row #5, Column 2 Row #5"

#2. %
"Column 7 Row #3"

#3. D
"Column 8 Row #7"

#4. a
"Column 7 Row #9"

#5. Dad
"'Column 8, Row #7', 'Column 7 Row #9','Column 0 Row #10'"

"Question 5"
#Write a python program that creates a car in the terminal.

print("   ___\n _|   |_ \n|       |\n|_______|\n  O   O")

#The line above is a print function with \n to create the shape of a car. 

"Question 6"

print(3, 2+5, 2>5, "Test!", "!", sep=' ', end='>>')
#"sep='@'" separates all the printed numbers/strings in place of a space like a spacebar gives you
#as long as the "2+5" and "2>5" are separated by commas, the interpreter will consider them to be statments and give you the answers whether it is false, like the "2>5", and "7" from the "2+5". 
#   3@7@False@Test!@!>> is the result of the print statement above. 

#if I were to change sep="@" to sep=" ", the print would show as
#   3 7 False Test! !>>

#take away only the "end='>>'"
#   3@7@False@Test!@!

#so on and so forth, what you take away is taken away from the end product, if I take away the "3" at the very beginning, the product would start with "7" instead of "3". 

