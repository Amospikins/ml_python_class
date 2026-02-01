# A function that remembers variables from its outer scope, even after that scope is gone.

def outer_function():
    x = 10
    
    def inner_function():
        return x
    
    return inner_function


fn = outer_function()

fn()  # returns 10, because inner_function remembers x from outer_function's scope

# that memory is called a closure

