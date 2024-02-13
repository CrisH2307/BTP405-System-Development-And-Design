def numList():
    userinput = input("Input the list of number: ")
    list = userinput.split()

    for i in range (len(list)):
        list[i] = int(list[i])
    print("User list: ", list)
    print("User sum list: ", sum(list))

numList()