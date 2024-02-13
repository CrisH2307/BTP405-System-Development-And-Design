def Exponention(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return a* Exponention(a, b - 1)
        

print(Exponention(2,3))