# 가장 큰 수 LEETCODE #179
# 삽입 정렬을 이용하여 풀이할 수 있다.
from typing import List

class Solution:
    # 문제에 적합한 비교 함수
    # 9와 30 중 어느 것을 더 먼저 둘 것인가의 문제는 다음과 같이 풀이하면 쉽게 알 수 있다. 930 vs 390
    @staticmethod
    def to_swap(n1: int, n2: int):
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        # i-1과 i를 비교해야 하므로 출발하는 인덱스가 1이다.
        i = 1
        while (i < len(nums)):
            # 일단 현재 기준점까지 끌고 온다.
            j = i
            while (j > 0 and self.to_swap(nums[j-1], nums[j])):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                # 이전과 비교해보며 swap시 그 이전을 본다. 그러기 위해서는 j를 한칸 더 뒤로 이동해야 한다.
                j -= 1
            i += 1
        # join 결과를 int로 바꾸면 만약에 "00"이 나올 경우 "0"으로 바꿀 수 있다.
        return str(int(''.join(map(str, nums))))