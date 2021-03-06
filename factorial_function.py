def factorial(n: int) -> int:
    """Return n! (0! is 1)."""
    if n <= 1:
        return 1

    result = 2
    for x in range(3, n + 1):
        result *= x

    return result


for i in range(36):
    print(i, factorial(i))

# 0 1
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120
# 6 720
# 7 5040
# 8 40320
# 9 362880
# 10 3628800
# 11 39916800
# 12 479001600
# 13 6227020800
