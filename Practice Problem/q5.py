def largestEle(arr):

    for i in range(1, len(arr)):
        if arr[i] > arr[0]:
            return arr[i] 


array = [33, 21, 2, 120, 49, 899]
print("Largest ele is: ", largestEle(array))