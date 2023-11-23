# Consider a text file such as ages.txt which represents the ages of a sample of students at the college.
# Ages are between 18 and 30
# Find and display the statistics, show the average, minimum age

def getData(filename):
    # right click the file and use "copy path" instead of just putting in the file name.
    while True:
        try:
            file = open(filename, 'r')
            content = file.read()
            file.close()
            strls = content.split()
            intls = [int(x) for x in strls]
            return intls
        except FileNotFoundError as err:
            print("Error-", err)
            filename = input("Enter a correct input file name: ")
        except ValueError as err2:
            print("Error-", err2)
            input("Fix the age in the input file and press a key to continue...")
            filename = input("Enter the input file name: ")


def frequencies(ls):
    d = {}
    #empty dictionary has been created
    for age in ls:
        # Validate ages:
        if age < 18 or age > 30:   # invalid data
            print("Error- invalid age", age)
            return None
        d[age] = d.get(age, 0) + 1
    return d


def stat(d):
    ls = d.keys()
    total = 0
    count = 0
    for age in ls:
        count += d[age]
        total += d[age] * age
    avg = int(total/count)
    return min(ls), avg


def displayFrequencies(d):
    for age in range(18, 31):
        freq = d.get(age, 0)
        print(age, freq*'-')


def main():
    infile = input("Enter the input file name: ")
    agesLs = getData(infile)
    myDict = frequencies(agesLs)
    if myDict != None:
        low, avg = stat(myDict)
        print("Minimum age is", low, "Average age is", avg)
        displayFrequencies(myDict)


main()
