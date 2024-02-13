def FibonacciSeq(n):
    newList = []
    a,b = 0,1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(FibonacciSeq(9)))
