#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow +=1
        print(slow)
        if slow == len(nums):
            return nums
        else:
            for item in range(slow, len(nums)):
                nums[item] = 0
        return nums
# @lc code=end

