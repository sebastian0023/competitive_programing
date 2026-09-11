def module_func(n,m):
    res = 0
    if n == 0:
        return 0
    while n-1 > 0:
        res += (n*n-1) % m
        res = res % m
        n -= 1
    return res

n = 100
m = 100000007
result = module_func(n, m)
print(f"The result of module_func({n}, {m}) is: {result}")