def coins(arr,target):
    dp = [0] * (target + 1)
    dp[0] = 1  # There's one way to make the target 0, which is to use no coins.



    for i in range(1, target + 1):
        for coin in arr:
            if i - coin >= 0:
                dp[i] += dp[i - coin]

    return dp[target]

arr = [2, 3, 5]
target = 9
result = coins(arr, target)
print(f"Number of ways to make {target} using coins {arr}: {result}")