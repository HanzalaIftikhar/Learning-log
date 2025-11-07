# This python script is about functions in python programming language

# 1st method of def a function
# def greet(): # defining a function
#     print("Hello, Welcome to Python programming")

# greet()  # calling the function to execute the function

# # 2nd function of def a function
# def greet():
#     text = "Hello, Welcome to Python programming"
#     print(text)

# greet()  # calling the function to execute the function

# # 3rd method
# def greet(text): # defining a function with parameter
#     print(text)

# greet("Hello, Welcome to Python programming")  # calling the function with argument

# # My function
# def add(a, b): # defining a function with parameters
#     result = a + b  # returning the sum of a and b
#     print("The sum is:", result)
    

# add(int(input("enter number ")), int(input("enter 2nd number ")))  # calling the function with arguments


# # def a function with  if elif and else 

# def school_calculator(age):
#     if age == 5:
#         print("You can go to Kindergarten")
#     elif age > 5:
#         print("You can go to high school")
#     else:
#         print("You are too young for school")        


# school_calculator(int(input("Enter age: ")))  # calling the function with argument


#def a function for future (mini machine learning project)

def future_age(name, age):
    years = int(input("Enter number of years to add: "))
    future_age= age + years
    print("Hello", name, "in", years, "years, you will be", future_age, "years old")
    return future_age
    

future_age(input("Enter your name: "), int(input("Enter your age: "))) # calling the function with arguments
