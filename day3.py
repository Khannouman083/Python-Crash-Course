# a simple python function 
def greet():
    print("Hello World")
greet()


#function in python can also take arguments
def newGreet(name):
    print(f"Hello {name}")
newGreet("Nouman")

#function can also take default arguments
def newestGreet(name="Nomii"):
    print(f"Hello {name}")
newestGreet()
newestGreet("Nouman")  

# functions can also return values which can be stored for future use
def multiply(a,b):
    return print(a*b)
multiply(2,6)


# Lambda functions are small, anonymous functions defined using the lambda keyword
# The syntax is lambda arguments: expression
subtract = lambda x,y: x-y
print(subtract(5,2))


