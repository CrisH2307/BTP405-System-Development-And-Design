def decoratorFunc(foo):
    def wrap(nums_str):
        str_num = nums_str.split()
        
        nums = []
        for num in str_num:
            nums.append(int(num))

        print("The numbers read: ", nums)
        print("The count of the numbers read: ", len(nums))
        print("The average of the numbers: ", sum(nums) / len(nums))
        print("The maximum of the numbers: ", max(nums))
        return foo(nums)
    
    return wrap

@decoratorFunc
def decorate(nums):
    print(nums)

def printStats(t):
    with open (t, 'r') as f:
        nums_str = f.readline()
        decorate(nums_str)

def main():
    printStats("q4.txt")


if __name__ == "__main__":
    main()

