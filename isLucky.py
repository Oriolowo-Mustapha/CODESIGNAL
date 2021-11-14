def isLucky(n):
    strN = str(n)
    digit_len = len(strN)
    half_len = (int)(len(strN) / 2)
    first_half = 0
    second_half = 0
    for i in range(0, half_len):
        first_half += int(strN[i])
    for i in range(half_len, len(strN)):
        second_half += int(strN[i])
    return first_half == second_half
