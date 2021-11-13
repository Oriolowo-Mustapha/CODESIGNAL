def almostIncreasingSequence(sequence):
    nun = len(sequence)
    if nun <= 2:
        return True
    numa = 0
    numaa = 0
    for i in range(1, nun-1):
        if sequence[i-1] >= sequence[i]:
            numa += 1
        if sequence[i-1] >= sequence[i+1]:
            numaa += 1
    if sequence[nun-1] <= sequence[nun-2]:
        numa += 1
    if numa <= 1 and numaa <= 1:
        return True
    else:
        return False