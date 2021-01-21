# 배열 파티션 I LEETCODE #561
# Pythonic Way로 풀어보는데, 이 때 슬라이싱을 이용한다.

def solution(nums):
    return sum(sorted(nums)[::2])