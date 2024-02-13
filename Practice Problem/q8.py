def countVowel(str):
    count = 0
    for i in range(len(str)):
        if (str[i].lower() == "a" or 
            str[i].lower() == "e" or
            str[i].lower() == "i" or
            str[i].lower() == "o" or
            str[i].lower() == "u" ):
            count += 1
    
    return count



word = "Count number of vowels in a String in Python"
print("Vowels: ", countVowel(word))