"""
CLOSURES
_ Is a nested function that has access to variables from its containing (enclosing) 
function's scope, even after the outer function has finished execution
_ This means that the inner function "closes over" the variables in the outer function,
retaining access to them
_ Allows you to encapsulate certain variables or parameters within a function, creating
a self-contained unit of behavior that can be configured when the closure is created
_ A closure is created when a nested function references a variable from its containing func

Advantages:
_ Encapsulation: Variables in the outer func can be encapsulated within the closure, 
providing a form of data hiding
_
"""


"""
BREAKDOWN:
_ Outer takes a param x and defines inner inside it
_ Inner is a closure because it references the variable x from the outer func
_ When the outer(10) is called, it returns the inner with x set to 10
_ The returned closure can be used independently and still has access to the value
of x from the outer function
"""
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(10)

# Now, closure is a func that remembers the value of x
res = closure(4)    # --> Returns 14 (10 + 4)
print(res)


#### Closure as a callback function
def callback_creator(prefix):
    def callback(message):
        print(prefix + ": " + message)
    return callback

# Creating callbacks with different prefixes
callback1 = callback_creator("Info")
callback2 = callback_creator("Warning")

callback1("This is the information message")
callback2("This is a warining message")