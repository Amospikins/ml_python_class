# A function that calls itself to solve a problem by breaking it into small pieces
# Rules of recursion:
# 1. Base Case: A condition under which the function stops calling itself: When to stop
# 2. Recursive Case: The part of the function where it calls itself with modified arguments: calls itself

# No base case => infinite loop => crash

# Example: Factorial of a number n (n!) = n * (n-1) * (n-2) * ... * 1

# def factorial(n):
#     # Base Case
#     if n == 0 or n == 1:
#         return 1
#     # Recursive Case
#     else:
#         return n * factorial(n - 1)
    
    
    # factorial(3)
    # = 3 * factorial(2)
    # = 3 * 2 * factorial(1)
    # = 3 * 2 * 1 * factorial(0)
    # = 3 * 2 * 1 * 1
    
    
    # countdown
    
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


countdown(5)