# print is used to print any of the data
print("Hello World")

#python follows 4 indentation by default
if(True):
    print("This is the if true statement")

# python do not require explicit decalaration of varaibles
x=22 #int
y=45.675  #float
z="Nouman" #str
w= True   #bool
a= 4+5j  #complex

# we can convert between different data types 
age= "22" # its a string
intAge = int(age)  #its now an int

# we can also check the data type of a variable
print(type(age))
print(type(intAge))

# print function display the output stream
print("My name is ",z)


#input function take the input from user
name = input("What is your name? \n")
print("Welcome", name)

#we can also convert a user name taken from the user to different data type
age = int(input("Enter your age:\n"))
print("Your age is:", age)

# some useful built in functions
print(len(name))

# we can also format output in python using fstring
print(f"Hello my name is {name} and i am {age} years old")
print("Hello my name is {0} and i am {1} years old".format(name,age))

# string concatenation and multiline strings
firstname ="Nouman"
lastName ="Khan"
fullname = firstname + " " +lastName
print(fullname)

description = """This is a multiline string
and it can expand
int multiple lines"""
print(description)


# Write a program that asks the user for their name and age, then prints a greeting using the information provided.
name = input("Enter your name: ")
age = input("Enter your age: ")
age= int(age)
print(f"Hello {name}, your age is {age} and next year you will be {age+1}")


# Write a program that calculates the area of a rectangle. Prompt the user for the width and height, then display the area.
height = int(input("Enter height: "))
width = int(input("Enter width: "))
area = height*width
print("The area of reactangle is", area)

# Create a program that converts a temperature from Celsius to Fahrenheit. Use the formula F = (C * 9/5) + 32.
celsius = float(input("Enter temprature is celsius: "))
fahrenheit = (celsius*9/5)+32
print("The tempearture is fahrenheit is {0}".format(fahrenheit))