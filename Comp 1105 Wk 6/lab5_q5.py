PI = 3.14

def main():
    #getData gets data from the user, aka input a number or value
    r = getData()
    #getArea takes the radius of the circle as a parameter and calculates the area of the circle. 
    a = getArea(r)
    
    print("Radius is %d, Area is, ", format(a, "0.2f"))

    a = getArea()
    print("Radius is 1, Area is ", format(a, ".2f"))


def getData():
    rad = int(input("What is the radius of the circle? "))

    if rad <= 0:
        print("Radius cannot be 0 or less")

getData()

def getArea(r):
#calculation to get the area of a circle:
    #area = PI * radius^2

    if r <= 0:
        print("radius of a cicle cannot be 0 ")
    else:
        area = PI * (r**2)
        
    
#if there is no radius given, the default radius will be set at a value of 1
getArea(r)

main()