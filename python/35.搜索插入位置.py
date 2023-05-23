#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1 
        r = len(nums)
        while l + 1 != r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        return r


            
# @lc code=end

