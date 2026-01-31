# FUNCTION IS A REUSABLE BLOCK OF CODE THAT PERFORMS A SPECIFIC TASK
# def greet():
#     print("Hello! Welcome to the program.")


# greet()

# functions with parameters

# def greet_user(name):
#     print(f"Hello, {name}! Welcome to the program.")

# greet_user("Amos")

# def sum(a, b):
#     c = a + b
#     return c

# result = sum(5, 10)
# print(result)

# DEFAULT PARAMETER VALUES
# def multiply (a, b, c = 6):
#     return a*b+c

# result = multiply(2, 3, 4)
# print(result)
    
# KEYWORD ARGUMENTS
def user_profile(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

user_profile(age=25, city="New York", name="Alice")
    