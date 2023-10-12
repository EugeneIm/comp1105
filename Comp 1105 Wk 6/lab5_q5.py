PI = 3.14

def main():
    r = getData()
    #this is calling the function with the value that you gave to r
    a = getArea(r)
    #%d is for decimal numbers
    #%.2f is the same as "format(..., '.2f')"
    #r is the radius given, a is the area. 
    print("Rad is %d, Area is %.2f" % (r, a))

    #this calls the function with the parameter that the radius of the circle is 10
    a = getArea(8)
    #we don't have r here because we hard coded the radius to be a certain value and we only care about formatting the AREA to be 2 decimal places
    print("Rad is 8, Area is ", format(a, ".2f"))

    #calling the function without any parameter. 
    #We ser the "radius = 1" so that if no parameters are given, the default radius is 1
    a = getArea()
    #no "r" in here as well because we are testing the "default" radius value of 1
    #only a is here and we format to 2 decimal places. 
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