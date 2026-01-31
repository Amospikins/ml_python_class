# a tuple is a collection of items that is ordered, immutable (cannot be changed), allows duplicate values and can store different datatypes

# Why tuples: data safety (accidentally change something)
# performance (tuples are faster than list)
# fixed records (things that should not change)

# Creating a tuple
# fruits = ("apply", "banana", "lemon")
# user = ("Amos", 28, True)

# x = (5,)

# print(type(x))

# Indexing
# indexing works like lists which means it starts from 0
# fruits = ("apply", "banana", "lemon")
# print(fruits[2])

# # negative indexing

# print(fruits[-3])


# slicing tuples
# number = (1,2,3,4,5)

# print(number[1:4])
# print(number[:3])
# print(number[::2])

# immutability
# you cannot modify a tuple
# fruits = ("apple", "banana")
# fruits[0] = "oranges"


# changing tuples (ojoro)
# fruits = ("apple", "banana")
# print(fruits)
# list_tuple = list(fruits)
# list_tuple.append("oranges")
# fruits = tuple(list_tuple)
# print(fruits)

# CONCATENATION
# a = (1,2)
# b = (3,4)
# c = a + b
# print(c)
# print(a * 3)
# print("Amos" * 3)

# colors = ("red", "green", "blue")
# for color in colors:
#     print(color)

# tuple built in functions
# nums = (10, 20, 30, 20)
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(nums.count(20))
# print(nums.index(20))

# location = (6.54335, 3.334545)