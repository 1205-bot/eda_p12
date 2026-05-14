memo = {0:1 , 1:1}

def fibonacci_asc(n):
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_asc(n - 1) + fibonacci_asc(n - 2)