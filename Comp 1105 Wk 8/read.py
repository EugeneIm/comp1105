# def getData(fname):
#     with open(fname, 'r') as data:
#         content = data.read()
#         split_content = content.split()
#         print(content)
#         print(split_content)
# getData('/Users/eugeneim/Desktop/COMP1105/comp1105/Comp 1105 Wk 8/two.txt')

def writeData(fname):
    with open(fname, 'w') as data:
        text = input("What do you want to write to the file?")
        data.write(text)
writeData('/Users/eugeneim/Desktop/COMP1105/comp1105/Comp 1105 Wk 8/two.txt')