def listPrime(arr):
    newList = []
    for i in arr:
        if i > 1:
            ok = True
            for j in range(2, i):
                if i % j == 0:
                    ok == False
                    break
            else:
                newList.append(i)
        
    return newList

array = [1,2,3,4,5,6,7,8,9, 10, 11, 12]
print("New list: " , listPrime(array))

