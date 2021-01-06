# LEETCODE 509
class Solution:
    dp = collections.defaultdict(int)

    # 메모이제이션 방식
    def fib_topDown(self, N: int) -> int:
        if (N <= 1):
            return N
        if (self.dp[N]):
            return self.dp[N]
        self.dp[N] = self.fib(N-1) + self.fib(N-2)
        return self.dp[N]

    # 타뷸레이션 방식
    def fib_bottomUp(self, N: int) -> int:
        self.dp[1] = 1
        for i in range(2, N+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[N]
    
    # 두 변수만 이용해 공간 절약
    def fib_optimization(self, N: int) -> int:
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x