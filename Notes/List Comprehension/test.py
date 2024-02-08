"""
LIST COMPREHENSION
_ Offers a shorter syntax when you want to create a new list
based on the values of an existing list

Ex:
Based on a list of fruits, you want a new list, containing only
the fruits with the letter "a" in the name

Formula:
    list = [i for item in iterable if condition == True]


"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

# With for Loop
for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

# With List Comprehension
newList = [x for x in fruits if "a" in x]
print(newList)


# Accept only numbers lower than 5
list1 = [1, 2,3,4,5, 34, 32, 0, 9, 94, 20, 7,6 ,78]
newnumList = [num for num in list1 if num < 5]
print(newnumList)

# Print the list of square
squares = [each**2 for each in range (12)]
print(squares)

# Print the list of square but Dictionary
squares = {each: each**2 for each in range (12)}
print(squares)