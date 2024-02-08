def wordCount(t):
    f = open(t, "r")
    dictionary = {}

    for line in f:
        line.strip()
        line.lower()
        words = line.split(" ")

    for aWord in words:
        if aWord in dictionary:
            dictionary[aWord] = dictionary[aWord] + 1
        else:
            dictionary[aWord] = 1

    for key in list(dictionary.keys()):
        print(key, ":", dictionary[key])

def main():
    print(wordCount("q3.txt"))
    

if __name__ == "__main__":
    main()