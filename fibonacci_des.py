dp = [1 , 1] 


def fibonacci_des(n):
    if n == 0 or n == 1:
        return dp[n]

    while len(dp) <= n:
        dp.append(dp[-1] + dp[-2])

    return dp[n]