def Permutation(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i] , a[l] 
            Permutation(a, l+1, r)
            a[l], a[i] = a[i] , a[l] 


string = "ABC"
n = len(string) 
a = list(string) 
Permutation(a, 0, n)
