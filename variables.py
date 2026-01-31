import math
# print("duasfgdshgj")
# distance = 100
# time = 9.58
# speed = distance / time
# print(speed)

# PYTHON OPERATORS (SIGNS FOR MATHEMATICAL OPERATIONS)
# +, -, *, /, %, **, // and =
# a = 10
# b = 2
# print(a%b)

# a = 5**2
# print(a)

# a = 11 // 2
# print(a)


# PYTHON DATATYPES
# NUMBERS
# int => whole numbers
# float => decimal numbers  
# complex => numbers with j(imaginary part) in it 46465436j

# STRINGS
# fullname = "Jane Doe"

# BOOLEAN (BOOL) true/false
# is_employed = True
# print(type(is_employed))




# COLLECTIONS)(built in data structures)
# 1. Lists => ordered, changeable, allows duplicate members
                           
fruits = ["apple", "banana", "cherry", "apple"]
# scores = [54,325,35,"ddfg", True, 54]
# print(fruits[0])
# fruits[0] = "orange"
# print(fruits[0])

# TUPLES => ordered, unchangeable, allows duplicate members
# colors = ("red", "green", "blue", "red")

# SETS => unordered, unindexed, no duplicate members
# unique_numbers = {1, 2, 3, 4, 4, 5}

# DICTIONARY (disc)
# => unordered, changeable, no duplicate members
person = {
    "name": "Amos",
    "age": 30,
    "is_developer": True,
    "skills": ["Python", "JavaScript", "Django"],
    "address": {"street": "123 Main St", "city": "Nairobi", "country": "Kenya"},
}

# person["name"] = "John Doe"

# print(person["skills"][0])
# age = "25"

# # TYPE CONVERSION
# age = "25"
# convertedAge = float(age)
# age = "25"
# convertedAge = int(age)



# Variable Naming Conventions in Python

# full_name = "Jane Doe"
# dateOfBirth = "Alice Smith"  # This will cause a syntax error due to the space
# date_of_birth = "1990-01-01"
# isEmployed = True



# ALMIGHTY FORMULA
# x1 = -b + √(b² - 4ac) / 2a
# x2 = -b - √(b² - 4ac) / 2a

# a = 1
# b = -8
# c = 5
# x1 = (-b + math.sqrt(((b**2) - (4*a*c))))/ (2*a)

# x2 = (-b - math.sqrt(((b**2) - (4*a*c))))/ (2*a)
# # fourAC = 4*a*c
# # twoA = 2*a
# # bSquar = b**2
# # squareRoot = math.sqrt(bSquar - fourAC)
# # x1 = (-b + squareRoot) / twoA
# # x2 = (-b - squareRoot) / twoA


# print(x1)
# print(x2)


# BMI CALCULATOR: bmi = weight(kg) / height(m)^2

# weight = 70  # in kilograms
# height = 2  # in meters
# bmi = weight / (height **2)
# print(bmi)

weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters: "))
bmi = weight/(height**2)
print(bmi)