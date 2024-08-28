#  list in Python is an ordered collection of items, which can be of any data type
fruits = ["Apple","Apple", "Mango", "Orange", "Guava"]

# print list and specfic elemetns
print(fruits)
print(fruits[0])

# Access elements from the end of the list using negative indices.
sports = ["Cricket", "Hockey", "Volley Ball", "Football"]
print(sports[-1])

# Retrieve a portion of the list by specifying a range.
print(sports[0:3])

# Lists are mutable, so you can change an element by accessing its index.
sports[3]="Badminton"
print(sports)

# Use append() to add an element to the end of the list, or insert() to add an element at a specific index.
fruits.append("Pineapple")
print(fruits)

fruits.insert(5,"Kiwi")
print(fruits)

# Use remove() to remove an element by value, or pop() to remove an element by index.
fruits.remove("Orange")
fruits.pop(2)
print(fruits)

# Use len() to find out the number of items in the list.
print(len(fruits))

fruits.clear()
fruits.sort()
fruits.reverse()
print(fruits.count("Apple"))
print(fruits)


# A concise way to create lists. It consists of brackets containing an expression followed by a for clause.
squares = [x**2 for x in range(10)]
print(squares)

squares = [x**2 for x in range(10) if x%2 == 0]
print(squares)


# A tuple is an ordered collection of items, similar to a list. 
# However, tuples are immutable, meaning once created, the elements within a tuple cannot be changed.

coordinates = (12,5,45)
print(coordinates[0])
print(coordinates[-1])
# coordinates[0] = 15 raise an error
myTuple = ("Nomii", "Khan", "Yousafzai")
print(myTuple)

# You can concatenate two or more tuples to create a new tuple.
newTuple = myTuple + ("Nouman", "Khan")
print(newTuple)


# Assign the values from a tuple to a sequence of variables.
x= myTuple[0]
print(x)

print(newTuple.count("Khan"))
print(myTuple.index("Khan"))
