# LEETCODE 169
from typing import List
import collections

class Solution:
    # 브루트 포스로 과반수 비교
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num
    # 다이나믹 프로그래밍
    # nums.count()로 한 번 카운트를 계산한 값은 저장해서 재활용한다.
    # 만약 계산되지 않았던 값이 들어온다면 항상 0이 된다. 그 때만 카운트를 계산하게 된다.
    def majorityElement_DynamicProgramming(self, nums: List[int]) -> int:
        # 자바스크립트에서는 Object로 선언하고 undefined로 비교하면 된다.
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            if counts[num] > len(nums) // 2:
                return num
    # 분할 정복 아이디어
    def majorityElement_DivideAndConquer(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        half = len(nums) // 2
        a = self.majorityElement_DivideAndConquer(nums[:half])
        b = self.majorityElement_DivideAndConquer(nums[half:])
        # 과반수 이상인 녀석을 택한다. 자바스크립트에서는 true일 때와 false일 때를 삼항 연산자로 별도로 지정해주어야 한다.
        return [b, a][nums.count(a) > half]
    # 파이썬다운 방식
    # 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트이므로 이를 바로 리턴하도록 한다.
    def majorityElement_PythonicWay(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]