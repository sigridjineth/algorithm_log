from typing import List
import collections

# LEETCODE 621
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            # n+1을 추출하는 이유는 마지막에만 순서가 다르게 나오도록 하는 예외 처리
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()
            if not counter:
                break
            result += n - sub_count + 1
        return result

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(Solution().leastInterval(tasks, n))