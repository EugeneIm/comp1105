fruits = ['apples', 'oranges', 'cherries', 'watermelon']
#insert an object into a specified index
fruits.insert(2, 'dragonfruit')
#print only a certain section of the list
print(fruits[0:2])
#shorthand loop to go through the list
[print(x) for x in fruits]
#append 'kiwi' to the list
fruits.append('kiwi')


def total():
    numbers = [1, 9, 23, 5, 2, 9]
    total_value = sum(numbers)
    sum_value = total_value/len(numbers)
    print(sum_value)
total()