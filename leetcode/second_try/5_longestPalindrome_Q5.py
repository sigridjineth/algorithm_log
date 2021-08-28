class Solution:
    def dynamic_programming(self, s: str) -> str:
        n = len(s)
        d = [[False] * n for _ in range(n)]
        # initalize
        x = 0
        y = 0
        # base 1: length = 1
        for i in range(n):
            d[i][i] = True
        # base 2: length = 2
        for i in range(n - 1):
            if (s[i] == s[i + 1]):
                d[i][i + 1] = True
                if (not x and not y):
                    x, y = i, i + 1
        # continue: length >= 3
        for k in range(2, n):
            for i in range(0, n - 2):
                j = i + k
                if (j >= n):
                    break
                if (d[i + 1][j - 1] == True and s[i] == s[j]):
                    d[i][j] = True
                    if ((j - i) > (y - x)):
                        x, y = i, j
        
        return s[x:y + 1]
      
    def expand(self, left: int, right: int, s: str) -> str:
        while (left >= 0 and right <= len(s) and s[left] == s[right - 1]):
            left -= 1
            right += 1
        return s[left + 1:right - 1]
    
    def longestPalindrome(self, s: str) -> str:
        if (len(s) < 2 or s == s[::-1]):
            return s
        result = ""
        for i in range(0, len(s)):
            result = max(result, self.expand(i, i + 1, s), self.expand(i, i + 2, s), key = lambda n: len(n))
        return result
      
