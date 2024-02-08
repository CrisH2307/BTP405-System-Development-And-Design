#Approach 1
def doubleL(n):
    res = []
    for i in range(n): res.append(i * 2)
    return res

for i in doubleL(5): 
    print(i, end=' : ')