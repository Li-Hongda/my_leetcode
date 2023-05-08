#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0
        for i, jump in enumerate(nums):
            if max_step >= i and i + jump > max_step:
                max_step = i + jump
        return max_step >= i
# @lc code=end

