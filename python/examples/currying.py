"""Example of implementation of currying on python."""
from functools import partial
from inspect import signature

def curry(fnc):
    def inner(arg):
        if len(signature(fnc).parameters) == 1:
            return fnc(arg)
        return curry(partial(fnc, arg))
    return inner

def add (a: int, b: int, c: int) -> int:
    return a + b + c

add_10 = partial(add,10)
add_10_100 = partial(add_10, 100)
print(add_10_100(1000))




    
@curry
def add_2(a,b,c):
    return a + b + c


# Direct call with currying
print(add_2(10)(20)(3000))

# Partial call with currying
add_2_partial = add_2(10)(20)
print(add_2_partial(1000))

