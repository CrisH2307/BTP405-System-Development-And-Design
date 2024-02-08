import matplotlib.pyplot as plt


def graphSnowfall(t):
    with open (t, "r") as f:
        for line in f:
            num_Falldata = [int(line.strip()) for line in f]

    ranges = [0, 10, 20, 30, 40, 50]
    cnt_range = [0] * (len(ranges) - 1)

    for eachFall in num_Falldata:
        for i in range (len(ranges) - 1):
            if ranges[i] <= eachFall < ranges[i + 1]:
                cnt_range[i] += 1

    plt.bar(
            [f"{ranges[i]}-{ranges[i+1]} cm" 
                    for i in range(len(ranges) - 1)], cnt_range)
    plt.xlabel('Snowfall Ranges (cms)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Distribution')
    plt.show()


graphSnowfall("q2.txt")

plt.show()

