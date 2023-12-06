#call a function within a function using factorials to create and end condition
#inside 'fact' you are calling 'fact'
    #without a base case, the call is infinite

# def fact(n):
#     if n == 1:
#         return 1
#     print(n)
#     return n * fact(n-1)
# result = fact(3)

# print(result)

# def recur(n):
#     #n = int(input("Put in a number"))
#     if n == 1:
#         return 1
#     print(n)
#     return n * recur(n-1)
# end = recur(9)
# print(end)

#GCD 

# def div(n, m):
#     if m == 0:
#         return n
#     return div(m, n%m)

# end = div(38, 12)   
# print(end)

# def fib(n):
#     if n == 1 or n == 2:
#         return n - 1
    
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(10))

#recursion to find the largest value in a list.
# def maxValue(ls):
#     #base case is always at the top of the function
#     if len(ls) == 1:
#         return ls[0]
#     #the length of the list is 1, give me the first element
#     newls = ls[1:]
#     x = maxValue(newls)
#     if x > ls[0]:
#         return x
#     else:
#         return ls[0]
# myls = [1, 252, 128, 921]

# maxValue(max(myls))

# def main():
#     num = 0
#     show_me(num)
# def show_me(arg):
#     if arg < 10:
#         show_me(arg + 1)
#     else:
#         print(arg)
# main()


# def traffic_sign(n):
#     loop/iteration version
#     while n > 0:
#         print('No Parking')
#         n = n - 1
#     recursive version
#     if n > 0:
#         print("park")
#         traffic_sign(n-1)
# traffic_sign(10)


#recursive function printing 1 through n 
# def f(n):

#     if n > 1:
#         f(n-1)
#     print(n)

# f(15)

#sum of numbers from 1 through n

def sum(n):

    if n > 1:
        numOne = n - 1
        numTwo = n - 2
        total = numOne + numTwo
    print(total)

sum(50)