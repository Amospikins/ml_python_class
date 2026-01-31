# LIST => ARRAY => SEQUENCE => list of elements (values) which can be or any data type:
# ordered, changeable, allows duplicate members

        
# fruits = ["apple", "banana", "cherry", "apple"]
            #  0    1    2    3       4    5
mixedList = [54, 325, 35, "Sanmi", True, 54.1]
# mixedList[0] = "Orange"
# print(mixedList[0])
# print(mixedList[-1])
# print(mixedList)

# Adding Items to a list
# mixedList.append("Tolu")
# mixedList.extend(["Tolu", "Amos"])
# mixedList.insert(0, "Adeola")  # insert at index 2
# print(mixedList)


# Removing Items from a list
# mixedList.remove(54)  # removes first occurrence of value 54
# mixedList.pop(1)
# del mixedList[2]  # deletes item at index 2
# print(mixedList)

# length of a list
# print(len(mixedList))

# Sorting a list
# numbers = [5, 2, 9, 1, 5, 6]
# # numbers.sort()
# numbers.sort(reverse=True)
# print(numbers)

# reverse a list

numbers = ['5', '2', '9', '1', '5', '6']
numbers.reverse()
print(numbers)

# user = {
#     "name": "Amos", 
#     "age": 30,
#     "is_developer": True,
# }

# users = [
#     {"name": "Amos", "age": 30, "is_developer": True,},
#     {"name": "Jane", "age": 25, "is_developer": False,},
# ]

# print(users[0]["name"])