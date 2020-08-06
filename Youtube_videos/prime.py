
import time
import math

def is_prime_v1(n):

    """Return 'True' if 'n' is a prime number. False otherwise"""

    if n == 1:
        return False # 1 is not a prime number

    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def is_prime_v2(n):

 
    """Return 'True' if 'n' is a prime number. False otherwise"""

    if n == 1:
        return False # 1 is not a prime number

    for d in range(2, 1 + (math.floor(math.sqrt(n)))):
        if n % d == 0:
            return False
    return True


def is_prime_v3(n):

 
    """Return 'True' if 'n' is a prime number. False otherwise"""

    if n == 1:
        return False # 1 is not a prime number

    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False


    for d in range(3, 1 + (math.floor(math.sqrt(n))), 2):
        if n % d == 0:
            return False
    return True

   



    # ====Time Function =======

t0 = time.time()
for n in range(1, 100000):
    is_prime_v1(n)
t1 = time.time()


t2 = time.time()
for n in range(1, 100000):
    is_prime_v2(n)
t3 = time.time()


t4 = time.time()
for n in range(1, 100000):
    is_prime_v3(n)
t5 = time.time()




print("Time taken for v1: ", t1-t0)
print("Time taken for v2: ", t3-t2)
print("Time taken for v2: ", t5-t4)

