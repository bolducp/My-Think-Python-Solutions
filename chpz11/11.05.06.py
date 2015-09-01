"""One solution is to keep track of values that have already been computed
by storing them in a dictionary. A previously computed value that is stored
for later use is called a memo. Here is a “memoized” version of fibonacci:

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
known is a dictionary that keeps track of the Fibonacci numbers we already
know. It starts with two items: 0 maps to 0 and 1 maps to 1.
Whenever fibonacci is called, it checks known. If the result is already
there, it can return immediately. Otherwise it has to compute the new value,
add it to the dictionary, and return it.

Exercise 6
Run this version of fibonacci and the original with a range of parameters
and compare their run times."""

import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

known = {0:0, 1:1}

def fibonacci2(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

start = time.time()
print fibonacci(10)
lapse_time = time.time() - start
print lapse_time

start = time.time()
print fibonacci2(10)
lapse_time = time.time() - start
print lapse_time
