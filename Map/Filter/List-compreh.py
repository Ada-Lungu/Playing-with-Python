
# 1. MAP
# PB: FUNCTION SQUARES

squares = []
for i in range(10):
    squares.append(i**2)
print squares


def square(numbers):
    squares = []
    for each_num in numbers:
         squares.append(each_num**2)
    return squares

numbers_list = [0,1,2,3,4]
print square(numbers_list)


def square(x):
    return x**2
squares = map(square, range(10))
print squares


# lambda x: x**2 # anonymus inline function

squares = map(lambda x:x**2, range(10)) # aplica functia data de lambda pe fiecare elem din obiectul/sequence-ul dat si returneaza-mi o lista
print squares

print map(lambda x:x**2, range(10))



# 2. FILTER ==> receives a boolean function and an object; applies the boolean function on each element of the given object and RETURNS A NEW LIST of the elements that returned TRUE from the function

smaller_than = filter(lambda x: x < 5, range(10))
print smaller_than


squares = map(lambda x:x**2, range(10))
special_squares = filter(lambda y: y>10 and y<50, squares)
print special_squares


# 3. LIST COMPREHENSION ==> [expression-involving-loop-variable FOR loop-variable IN sequence] takes each element from the sequence, sets the loop-variable equal to each one, and then performs the expression for each one
#==> is more easily readable code than map and compact code

squares = [x**2 for x in range(10)]
print squares

special_squares = [x**2 for x in range(10) if x**2 < 50 and x**2 > 5]
print special_squares

squares = [x**2 for x in range(10)]
special_squares = [square for square in squares if 5 < square < 50 ]
print special_squares



#PB Names:

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

lengths = []
for name in names:
    lengths.append(len(name))
print lengths

lengths = map(lambda name: len(name), names)
print lengths

lengths = [len(name) for name in names]
print lengths

lengths = map(len, names)
print lengths

a_names = filter(lambda name: name[0]=="A", names)
print a_names

a_names = [name for name in names if name[0]=="A"] # list comprehension
print a_names


name_infos = [[name, name[0],len(name)] for name in names]
print name_infos

print [name[-1] for name in names]
print [name[::-1] for name in names]


# PB build up a new list from elements of/ looping over nested lists

possible_choices = []
for drink in ['water', 'tea', 'juice']:
    for food in ['ham', 'eggs', 'spam']:
        possible_choices.append([drink,food])
print possible_choices

drinks = ['water', 'tea', 'juice']
foods = ['ham', 'eggs', 'spam']

possible_choices = [[drink,food] for drink in drinks for food in foods]
print possible_choices


#PB







