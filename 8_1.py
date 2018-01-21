# Write a method to generate the nth Fibonacci number

def fib(n):
    if n == 0 or n == 1:
        return 1

    return fib(n-1) + fib(n-2)

assert(fib(5) == 8)
assert(fib(6) == 13)
assert(fib(0) == 1)
assert(fib(1) == 1)
