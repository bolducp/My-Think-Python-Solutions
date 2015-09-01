"""Memoize the Ackermann function from Exercise 5 and see if memoization
makes it possible to evaluate the function with bigger arguments.
Hint: no. """


cache= {}

def ackermann(m, n):
    if (m, n) in cache:
        return cache[(m, n)]
    if m == 0:
        solution = n + 1
        cache[(m, n)] = solution
        return solution
    if n == 0:
        solution = ackermann(m -1, 1)
        cache[(m, n)] = solution
        return solution
    solution = ackermann(m-1, ackermann(m, n-1))
    cache[(m, n)] = solution
    return solution


def ackermann2(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann2(m-1, 1)
    if (m, n) in cache:
        return cache[m, n]
    cache[m, n] = ackermann2(m-1, ackermann2(m, n-1))
    return cache[m, n]