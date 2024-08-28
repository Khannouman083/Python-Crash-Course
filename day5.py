# A set is an unordered collection of unique elements. Unlike lists or tuples, sets do not allow duplicate elements

# we can declare a set in 2 ways
mySet = {1,2,3,4,5,6,7}
mySet2 = set(["Mango", "Apple", "Banana","Guava"])
# The second method will automatically remove any duplicates.

# Union (|): Combines elements from two sets, removing duplicates.
newSet = mySet | mySet2
print(newSet)

# Intersection (&): Returns elements common to both sets
newSet2 = newSet & mySet
print(newSet2)

# Difference (-): Returns elements in the first set but not in the second.
newSet3 = mySet - mySet2
print(newSet3)

# Symmetric Difference (^): Returns elements in either set but not in both
newSet4 = mySet ^ mySet2
print(newSet4)

# some useful set methods
mySet2.add(11)  # Adds an element to the set.
mySet2.remove("Mango") # Removes the specified element. Raises KeyError if the element is not found.
mySet2.discard("Mango") # Removes the specified element if it exists. Does nothing if the element is not found.
mySet2.pop() # Removes and returns an arbitrary element from the set.
mySet2.clear() # Removes all elements from the set.
mySet2.update([11,15])
print(mySet2) 


# dictionary in Python is an unordered collection of key-value pairs

# we can create dictionary by two methods
my_dict = {"name" : "Nouman", "age" : 21, "Male" : True}
myDict2 = dict(name= "Nomii", age = 20, Male=True)

# You can access a value using its key.
print(my_dict['name'])
print(myDict2["name"])

# Adding or modifying key-value pairs: Simply assign a value to a key.
myDict2["name"] = "Noman Khan Yousafzai"
print(myDict2)

# Deleting key-value pairs: Use del or pop().
del myDict2["name"]
print(myDict2)
myDict2.pop("age")
print(myDict2)

# Checking if a key exists: Use the in keyword.
present = "name" in myDict2
print(present)

# some useful dictionary method
keys =my_dict.keys()
values = my_dict.values()
items = my_dict.items()
print(keys)
print(values)
print(items)
print(my_dict.get("Nomii", "Name not Found"))
my_dict.update({"class" : 1})
print(my_dict)

# Basic Dictionary Comprehension
squares = {x: x*x for x in range(6)}
print(squares)

evensquares = {x: x*x for x in range(6) if x%2==0}
print(evensquares)


oddSquares = {x: x*x for x in range(10) if x%2!=0}
oddValues = oddSquares.values()
print(oddValues)