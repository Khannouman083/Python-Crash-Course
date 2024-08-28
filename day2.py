# Control Structure is used to control the flow of execution of program

# if the condition in true then the statement below this condition will be executed
age=int(input("Enter your age: "))
if(age>=18):
    print('You are eligible to vote')

# elif stands for "else if" and is used to check multiple conditions. It is checked if the previous if or elif statement was False.
marks=int(input("Enter your marks: "))
if(marks>=90):
    print('Grade A')
elif(marks>=80 and marks<90):
    print('Grade B')   
elif(marks>=70 and marks<80):
    print("Grade C")

# The else statement is used when all the previous conditions are False. The code inside the else block is executed in that case.
if(age>=18):
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

# Loops allow you to execute a block of code multiple times.

# for loop
for i in range(5):
    print(f"Hello from {i}")

number = [1,3,5,7,9]
for num in number:
    print(f"Hello from {num}")

# while
count = 0
while count<5:
    print("Count is:",count)
    count+=1

# Break Statement: The break statement is used to exit the loop prematurely when a certain condition is met.
for i in range(10):
    if(i==5):
        break
    print(i)

# The continue statement is used to skip the current iteration of the loop and proceed to the next one.
for i in range(10):
    if(i==5):
        continue
    print(i)



# Write a program that checks if a given number is positive, negative, or zero using an if-elif-else statement.
num = int(input("Enter a number: "))
if(num==0):
    print("The number is zero")
elif(num>0):
    print("The nnumber is positive")
else:
    print("The number is negative")

# Create a for loop that prints out the numbers 1 to 10, but skip the number 7 using the continue statement.
for i in range(11):
    if(i==7):
        continue
    print(i)


# Write a while loop that asks the user for input repeatedly until they type the word "exit."
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter something:")
print("Goodbye!")
