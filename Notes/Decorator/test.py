"""
DECORATOR
_ Is a tool that allows you to modify the behavior of functions or class at runtime
_ Allows us to wrap another function in order to extend the behavior of of the wrapped 
function, without pernamently modifying it
_ It is higher-order functions that take another function as input and return a new function,
which usually extends or enhances the behavior of the original function
_ Decorators are commonly used to add additional functionality, logging, caching, authorization,
validation, etc,... to functions without modifying their source code directly.
_ Is denoted using the @decorator_name syntax immediately above the function definition. When the
decorated function is called, the decorator is applied to it before execution
"""


"""
BREAKDOWN
_ We define a custom decorator function my_decorator. The decorator takes a function func as input
and returns a new function wrapper, which adds the extra functionality before and after the original
function call. The wrapper function calls the original func and returns it result
_ WHen we apply the @my_decorator syntax above the say_hello function definition, it means that the 
say_hello function will be passed as an argument to the my_decorator function. Thus, say_hello is wrapped
inside the wrapper function, and whenever say_hello is called, the wrapper function with added behavior 
will be executed

"""
###### Custom decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func (*args, **kwargs)
        print("After execution")
        return result
    return wrapper

# Applying the decorator to a function
@my_decorator
def say_hello(name):
    return f"Hello, {name}"

# Calling the decorated function
greeting = say_hello("Cris")
print(greeting)


####### Custom Decorator with Arguments
def repeat(n):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return my_decorator

@repeat(4)
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Sean")


### Another Example

# defining a decorator
def hello_decorator(func):
 
    # inner1 is a Wrapper function in 
    # which the argument is called
     
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")
 
        # calling the actual function now
        # inside the wrapper function.
        func()
 
        print("This is after function execution")
         
    return inner1
 
 
# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")
 
 
# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)
 
 
# calling the function
function_to_be_used()
