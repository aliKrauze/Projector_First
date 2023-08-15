def result_cash(func):
    def wrapper(*args, **kwargs):
        memo = {}
        if args in memo:
            return memo[args]
        else:
            rv = func(*args)
            memo[args] = rv
            return rv
    return wrapper


@result_cash
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


try:
    n = int(input("Please enter a number of iterations"))
    fib_series = fibonacci(n)
    print(f"Fibonacci series {fib_series}")
except ValueError as e:
    print(e)
