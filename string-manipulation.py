# name = "Sanmi"
# message = 'sanmi is awesome'
# bio="""Sanmi is a software developer.
# He loves coding in Python.  He also enjoys teaching others."""
# # 01234
# # Sanmi

# text = "Python"
# # print(text[1])
# # text[2] = "a"  # This will raise an error because strings are immutable
# # Slicing

# print(text[2:4])  # 'Pyt'
# print(text[:5])  # 'Pytho'
# print(text[:])
# print(text[-4:]) # 'thon'

# # String Methods
# sample_text = "     hello, World! Welcome to Python programming.    "
# print(sample_text.upper())
# print(sample_text.lower())
# print(sample_text.title())
# print(sample_text.capitalize())

# # Stripping whitespace
# # print(sample_text.strip())
# print(sample_text.strip())
# print(sample_text.lstrip())
# print(sample_text.rstrip())
# #  Searching
# print(sample_text.startswith(" "))
# print(sample_text.endswith(" dxfasdf"))
# print(sample_text.find("World"))
# print(sample_text.count("o"))
# print(sample_text.replace("Python", "JavaScript")) 
# +234

# # first access the csv file (data.csv)
# with open("data.csv", "r") as file:
#     dataReadFromCSV = file.read()
#     print(dataReadFromCSV)

# string1 = "Hello"
# string2 = "World"
# print(string1 + " " +string2 + " This is another word" + " " + "!" )


# Format Strings
fullName = "Sanmi Ade"
age = 25
address = "Lagos"
gender = "Male"
# Using f-strings (Python 3.6+)
# print(f"My name is {fullName}. I am {age} years old, live in {address}, and I")
# print(f"My name is {fullName}. I am {age} years old, live in {address}, and I am {gender}.")

# format method
# print("My name is {}. I am {} years old, live in {}, and I am {}.".format(fullName, age, address, gender))
# STRING INTERPOLATION OR TEMPLATE LITERALS
# Split means breaking string into parts
# it means converting strings into list (Array)
# text = "Python is awesome, james, blabla"

# # print(text.split())
# print(text.split(","))


# Join means converting list (Array) into string

# words = ["Python", "is", "awesome"]
# print(" ".join(words))

# Write a program that tells if a word is a palindrom or not