def getStatToDelete(stats):

    savedStats = stats.copy()
    lenn = len(savedStats)

    for i in range(lenn):
        savedStats.pop(i)
        allSum = 0

        for j in range(len(savedStats)):
            if j % 2 == 0:
                allSum += savedStats[j]
            else:
                allSum -= savedStats[j]

        if allSum == 0:
            return i+1
        else:
            savedStats = stats.copy()

    return "NOT IN CASE"

print(getStatToDelete([1,3,4,3]))