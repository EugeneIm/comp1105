#call a function within a function using factorials to create and end condition
#inside 'fact' you are calling 'fact'
    #without a base case, the call is infinite

def fact(n):
    if n == 1:
        return 1
    print(n)
    return n * fact(n-1)
result = fact(3)

print(result)

def recur(n):
    #n = int(input("Put in a number"))
    if n == 1:
        return 1
    print(n)
    return n * recur(n-1)
end = recur(9)
print(end)

#GCD 

def div(n, m):
    if m == 0:
        return n
    return div(m, n%m)

end = div(38, 12)   
print(end)

def fib(n):
    if n == 1 or n == 2:
        return n - 1
    
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))