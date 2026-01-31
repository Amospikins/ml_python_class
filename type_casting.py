x = "5"
y = int(x)  #cast to integer
# Two types of type conversion
# Implicit conversion - done automatically by Python
# Explicit conversion (Type casting) - done manually by you

# Implicit: python automatically converts one data type to another when it is safe
# numInt = 10
# numFloat = 2.3
# result = numInt + numFloat

# print(result)
# print(type(result))

# Explicit type conversion
# int() float() str() bool() list() typle() set()

# x = "5.13"
# y = float(x)

# x = 100
# y = str(x)  # "100"

# print(bool(0))
# print(bool(1))
# print(bool(""))
# print(bool("Hello"))
# Empty = false(0,"",[], {})
# Anything = true
# text ="Hello"
# convertToList = set(text)
# print(convertToList) 

age = int(input("Enter your age: "))
if age>= 19:
    print("You are an adult")
else:
    print("You are a minor")