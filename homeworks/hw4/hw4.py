import numpy as np

#2 List slicing and striding
#2.1 Part 1
int50 = range(50)

#################################################
#2.2 part2

# Errors:
# SyntaxError: 'return' outside function - was missing indent before return
# NameError: name 'output' is not defined - was missing output declaration
# TypeError: unsupported operand type(s) for ** or pow(): 'range' and 'int - had extra square brackets on list_to_be_squared
def squarefunction():
    list_to_be_squared = range(10)
    output = []
    for integer in list_to_be_squared:
        output.append(integer**2)

    return output

#print (squarefunction())

#####################################################
#2.3 part3
#errors: TypeError: unsupported operand type(s) for +: 'range' and 'range'- casted a range to a list 

def odd_find():
    listA = list(range(10))
    listB = list(range(20,31))
    newlist = listA + listB
    oddlist = []
    for integer in newlist:
        if integer % 2 != 0:
            oddlist.append(integer)
    return list(set(oddlist))

#print(odd_find())
#list(set()) used to change list to set and then back ot list to remove duplicates and sort
###################################################

#3 2D Lists
#3.1 Part 1
#errors:none
array = []
for y in range(5):
    inner_array = []
    for x in range(5):
        inner_array.append(5*y+x+1)
    array.append(inner_array)
print(array)

##############################################################
#3.2 part 2

for y in range(5):
    for x in range(5):
        if array[y][x] % 3 == 0:
            array[y][x] = "?"
print(array)

###################################################      
#4 More List Practice
#error none
def remove_duplicates():
    duplicates = [1, 1, 2, 2, 3, 3, 4, 4]
    return list(set(duplicates))

#print(remove_duplicates())


