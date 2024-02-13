def GreatestCommonDivisor(a, b):
    """
    while b:
        a, b = b, a%b
    return a
    """
    return a if not b else GreatestCommonDivisor(b, a%b)


print(GreatestCommonDivisor(24, 60))