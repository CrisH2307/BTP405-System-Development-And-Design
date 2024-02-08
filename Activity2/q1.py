def getPrimeNumbers(n):
    arr = []
    if n > 1:
        for i in range (2, n):
            ok = True
            for j in range (2, i):
                if (i % j) == 0:
                    ok = False
                    break
            if ok:
                arr.append(i)
    return arr

def main():
    print(getPrimeNumbers(12))


if __name__ == "__main__":
    main()




