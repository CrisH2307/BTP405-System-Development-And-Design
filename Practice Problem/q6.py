def palindrome(str):
    if (len(str) % 2 == 0):
        half = len(str) // 2
        word1_temp = []
        for i in range(half):
            word1_temp.append(str[i])
        word1 = ''.join(word1_temp)
  
        word2_temp = []
        for i in range(half, len(str)):
            word2_temp.append(str[i])
        word2 = ''.join(word2_temp)
 
        if (word1.lower() == word2[::-1].lower()):
            print("This is palindrome")
        else:
            print("NO")
    else:
        half = (len(str) - 1) // 2
        word1_temp = []
        for i in range(half):
            word1_temp.append(str[i])
        word1 = ''.join(word1_temp)
  
        word2_temp = []
        for i in range(half + 1, len(str)):
            word2_temp.append(str[i])
        word2 = ''.join(word2_temp)
 
        if (word1.lower() == word2[::-1].lower()):
            print("This is palindrome")
        else:
            print("NO")
        
palindrome("Peelwleep")



## or

def isPalindrome(str):
    return str == str[::-1]

# Driver code
str = "malayalam"
ans = isPalindrome(str)
 
if ans:
    print("Yes")
else:
    print("No")