def allLongestStrings(inputArray):
    n = len(max(inputArray, key= len))
    return [s for s in inputArray if len(s) == n]
   
