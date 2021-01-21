# LEETCODE #46 Permutation DFS를 활용한 순열 생성

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(prefix, remain):
            if (not remain):
                return answer.append(prefix[:])
            for i in range(len(remain)):
                prefix.append(remain[i]) # A13
                dfs(prefix, remain[:i] + remain[i+1:])
                prefix.pop()
        answer = []
        dfs([], nums)
        return answer