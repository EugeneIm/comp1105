PI = 3.14

def main():
    r = getData()
    #this is calling the function with the value that you gave to r
    a = getArea(r)
    print("Rad is %d, Area is %.2f" % (r, a))

    #this calls the function with the parameter that the radius of the circle is 10
    a = getArea(10)
    print("Rad is 10, Area is ", format(a, ".2f"))

    #calling the function without any parameter. 
    #We ser the "radius = 1" so that if no parameters are given, the default radius is 1
    a = getArea()
    print("Rad is 1 (default radius), Area is ", format(a, ".2f"))

def getData():
    #This is giving the "r" the value in the main function
    rad = int(input("What is the radius of the circle? "))
    if rad <= 0:
        #radius can't be less than or equal to zero
        rad = int(input("The radius cannot be 0 or lower"))
    else:
        #returns the value so that r is given an actual value
        return rad

def getArea(radius = 1):
    #area is just the equation to get the area of the circle
    area = (PI * (radius**2))
    return area

main()