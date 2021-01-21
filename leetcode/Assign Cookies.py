class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if (index > result):
                result += 1
        return result