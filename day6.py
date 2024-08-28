# Strings in Python are sequences of characters, and they are one of the most commonly used data types.

# You can concatenate (join) two or more strings using the + operator.
hello = "Hello"
world = "World"
new= hello + " " + world
print(new)

# You can repeat a string multiple times using the * operator
laugh = "Ha"
print(laugh*3)

# Strings are indexed starting from 0. You can access individual characters using their index.
print(hello[1])
print(world[0])

# You can extract a substring from a string using slicing.
print(hello[1:4])

# .upper() and .lower(): Convert the string to uppercase or lowercase.
print(hello.upper())
print(world.lower())

# .strip(): Remove leading and trailing whitespace (or specified characters).
text= "          Hello  "
print(text.strip())

# .replace(old, new): Replace occurrences of a substring with another substring.
text1 = "Hello World"
print(text1.replace("World", "Nouman"))

# .split(delimiter): Split the string into a list of substrings based on a delimiter.
text2= "Hello,World,Python"
words = text2.split(",")
print(words)

# .join(iterable): Join a list of strings into a single string with a specified separator.
text3= " ".join(words)
print(text3)

# String Formatting Using % Operator
name="Nouman"
age=21
print("My name is %s and i am %d years old" % (name,age))

