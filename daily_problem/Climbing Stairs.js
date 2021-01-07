// LEETCODE #70
// 피보나치 수열을 떠올리는 재귀 구조 브루트 포스
let climbStairs_bruteForce = function(n) {
    if (n === 1) return 1
    if (n === 2) return 2
    return climbStairs(n - 1) + climbStairs(n - 2)
};

let dp = {}
let climbStairs_dp = function(n) {
    if (n === 1) return 1
    if (n === 2) return 2
    if (dp[n]) return dp[n]
    dp[n] = climbStairs_dp(n - 1) + climbStairs_dp(n - 2)
    return dp[n]
}

console.log(climbStairs_dp(38))