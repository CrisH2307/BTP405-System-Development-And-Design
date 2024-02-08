"""
CALLABLE
_ A build-in function that we can use to check if an obj is callable, it can be 
called like a function. Generally returns True if the obj can be called
_ A Callable Objs are objs that can be called as functions

When can I use a callable obj?
_ Functionality Extension: You can provide additional functionality or behavior when
an obj is called. This allows you to customize the behaviour of an instance beyond
what is possible with just regular method calls.
_ Stateful Objs: Instances of callable classes can maintain internal state, and calling
the instance can be used to modify or query that state. This is useful when you want an 
obj to encapsulate both data and behavior
_ Decorator-Like behavior: Callable objs are often used to create decorators. By defining
a callable class with a __call__ method. Instances of that class can be used to wrap functions
or methods, much like a decorator


"""

from typing import Any


x = 10

print(callable(x))

def foo(x):
    return x

y = foo
print(callable(y))


###################

class CallableObj:
    def __call__(self, x):
        return x* 2
    
foo = CallableObj()
res = foo(212)
print(res)