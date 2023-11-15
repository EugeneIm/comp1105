# every object in a set has to be unique
# elements can be different data types
# no particular order

# i.e. it can be a list/string/tuple

string_one = {'string one'}
print(string_one)

string_two = string_one.add('string two')
print(string_one)

string_three = string_one.update([1241])
print(string_one)

set_one = "asdf"
set_two = "jkl;"
set_one = set_one.join(set_two)
print(set_one)

intersect_one = set(('12345'))
intersect_two = set(('67890'))
intersect_three = intersect_one.intersection(intersect_one)
print(intersect_three)
