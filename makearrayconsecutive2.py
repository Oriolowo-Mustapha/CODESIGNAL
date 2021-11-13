def makeArrayConsecutive2(statues):
    record = 0
    statues.sort()
    for i in range(len(statues) -1):
        if statues[i + 1] - statues[i] >  1:
            record += statues[i + 1] - statues[i] - 1
    return record