from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 값이 오르는 경우 매번 계산
        for i in range(len(prices) - 1):
            if (prices[i+1] - prices[i]):
                result += prices[i+1] - prices[i]
        return result
    def maxProfit_Pythonic(self, prices: List[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))