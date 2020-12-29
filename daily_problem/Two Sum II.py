# LEETCODE 167 - Two Sum II, Input array is sorted
from typing import List
import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for (k, v) in enumerate(numbers):
            expected = target - v
            nums = numbers[k+1:]
            i = bisect.bisect_left(nums, expected)
            if (i < len(numbers[k+1:]) and numbers[i+k+1] == expected):
                return k+1, i+k+2
    def twoSum_noSlicing(self, numbers: List[int], target: int) -> List[int]:
        for (k, v) in enumerate(numbers):
            expected = target - v
            # bisect.bisect_left(a, x, lo=0, hi=len(a))
            # lo를 이용하면 bisect 모듈의 이진 탐색에서 왼쪽 범위를 제한할 수 있다.
            i = bisect.bisect_left(numbers, expected, k+1)
            if (i < len(numbers) and numbers[i] == expected):
                return k+1, i+1