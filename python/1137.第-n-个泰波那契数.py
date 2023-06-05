#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n+1)
        if n <=1:
            return n
        elif n <3:
            return 1        
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]

# @lc code=end

