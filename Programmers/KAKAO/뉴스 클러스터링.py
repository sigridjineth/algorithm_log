from collections import Counter
import re

def solution(str1, str2):
    str1s = [
        str1[i:i + 2].lower()
        for i in range(len(str1) - 1)
        if (re.findall('[a-z]{2}', str1[i:i + 2].lower()))
    ]
    str2s = [
        str2[i:i + 2].lower()
        for i in range(len(str2) - 1)
        if (re.findall('[a-z]{2}', str2[i:i + 2].lower()))
    ]
    
    intersections = sum((Counter(str1s) & Counter(str2s)).values())
    union = sum((Counter(str1s) | Counter(str2s)).values())
    
    if (union == 0):
        jaccard_sum = 1
    else:
        jaccard_sum = (intersections / union)
    
    return int(jaccard_sum * 65536)
