#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
# 快慢指针解法1 可能错过最优解，例[2,9,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]，
# 在两个9之间更新了最大值，此时left指针在第一个9，继续遍历到末尾，
# 能得到的最大值为len(nums) - left, 错过了真正的最大值从2到最后的1.
# Tips: 不应该根据当下的最值来更新left和right，而是不断遍历数组来更新最大值

class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     maxvol = 0
    #     left = 0
    #     for right in range(1, len(height)):
    #         for item in range(left, right):
    #             vol_temp = (right - item) * min(height[right], height[item])
    #             if vol_temp > maxvol:
    #                 maxvol = vol_temp
    #                 left = item
    #     return maxvol

# 所以
    def maxArea(self, height: List[int]) -> int:
        maxvol = 0
        right = len(height) - 1
        # for left in range(len(height)):
        left = 0
        while left < len(height):
            vol = (right - left) * min(height[right], height[left])
            maxvol = max(maxvol, vol)
            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1
            if right == left:
                break
        return maxvol    
# @lc code=end

