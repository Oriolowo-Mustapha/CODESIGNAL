from collections import Counter

def commonCharacterCount(s1, s2):
    common_letters = Counter(s1) & Counter(s2)  
    return(sum(common_letters.values()))