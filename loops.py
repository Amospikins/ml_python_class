import numpy as np

# Loops lets our code repeat certain actions => automatically, instead of writing the same line over and over

# numbers = [1,3,54,6,6,7,7]
# For loop and While Loop

# For loop is used to iterate => go through a sequence, e.g. collections

# for i in range(5):
#     print(i)
# start, stop, step
# # step and start are optional
# print(range(10))

# for tolu in numbers:
#     print(tolu + 2)

# fruits = ["apple", "banana", "pepper", "dates"]

# for fruit in fruits:
#     print(f"I like {fruit}")



# Whileloop
# while loop dey repeat as long as a condition is true

# count = 1

# while count <=5:
#     print("Count is:", count)
#     count += 1

# break => stops the loop early


# for num in range(10):
#     if num == 5:
#         continue
#     print(num)
# for num in range(10):
#     if num == 5:
#         break
#     print(num)

# print all even numbers from 1 to 10
# number = [2, 4, 5, 6, 7, 8, 9, 23,12,146,5432,3456,78786]
# for num in range(1, 1000000):
#     if num % 2 == 0:
#         print(f"{num} is an even number from the array")



# evens = [f"{num} is an even number from the array" for num in range(1, 1000000) if num % 2 == 0]

# print("\n".join(evens))


# numbers = np.arange(1, 1000000)
# even_numbers = numbers[numbers % 2 == 0]

# print(even_numbers)

def even_numbers():
    for num in range(1, 1000000):
        if num % 2 == 0:
            yield f"{num} is an even number from the array"

for msg in even_numbers():
    print(msg)