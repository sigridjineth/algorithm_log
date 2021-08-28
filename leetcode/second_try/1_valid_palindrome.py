# Valid Palindrome Q1125
class Solution:
    def usingSlicing(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]', '', s.lower())
        return s == s[::-1]
      
    def usingList(self, s: str) -> bool:
        strings = []
        for str in s:
            if (str.isalnum()):
                strings.append(str.lower())
        while (len(strings) > 1):
            if (strings.pop(0) == strings.pop()):
                continue
            else:
                return False
        return True
