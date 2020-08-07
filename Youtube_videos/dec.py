
# How to use decorators 

# calculate time taken by each function

from time import time

def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed', after - before)
        return rv
    return f



@timer
def add(x, y):
    return x + y


print(add(20,50))
print(add(10000, 5000000))