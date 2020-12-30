# LEETCODE 76
# 투 포인터 및 슬라이딩 윈도우로 최적화하자.
# 계속 우측으로 이동하는 슬라이딩 윈도우이면서 적절한 위치를 찾았을 때,
# 좌우 포인터의 크기를 좁혀나가는 투 포인터로 풀이할 수 있다.
import collections

def minWindow(s: str, t: str) -> str:
    need = collections.Counter(t)
    missing = len(t)
    left = start = end = 0

    # 오른쪽 포인터를 이동하자
    # 오른쪽 포인터의 값인 right을 하나씩 늘려나간다
    # 슬라이딩 윈도우의 크기가 점점 더 커지는 형태가 되는데, right은 1부터 시작한다. 슬라이딩 때문이다.
    # 만약 현재 문자가 필요한 문자 need[char] 에 포함되어 있다면 missing과 함께 1을 감소한다.
    for right, char in enumerate(s, 1):
        missing -= (need[char] > 0) # if true, minus 1
        need[char] -= 1
        # 필요 문자가 0이 되면 왼쪽 포인터를 이동한다.
        if missing == 0:
            while (left < right and need[s[left]] < 0): # 더 줄일 수 있는지 판단 여부는 음수이다.
                need[s[left]] += 1
                left += 1
            if not end or (right - left) <= (end - start):
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]

S = "ADOBECODEBANC"
T = "ABC"
print(minWindow(S, T))