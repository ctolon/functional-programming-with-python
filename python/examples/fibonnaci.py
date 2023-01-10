"""Example for generate fibonnaci series with generators"""

a,b,i = 0,1,0 # initial values

n = 10

def fibonacci_generator(n = None):
    global a,b,i
    if n is None:
        while True: # infinite generator
            a,b = b, a+b
            i = i+1
            yield a
    else:
        while True and i < n: # finite generator
            a,b = b, a+b
            i = i+1
            yield a
 
# Finite example (first 10 element in fibonnaci)        
iter_1 = fibonacci_generator(n)
t = tuple(iter_1)
print("First 10 element: ")
print(t) # first 10 element
print("\n===================\n")

# infinite example
iter_2 = fibonacci_generator()
print("11. element:")
print(next(iter_2)) # 11. element
