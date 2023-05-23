#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeft(nums: List[int], target: int) -> List[int]:
            l = -1 
            r = len(nums)
            while l + 1 < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m
                else:
                    r = m
            return r
        
        def searchRight(nums: List[int], target: int) -> List[int]:
            l = -1 
            r = len(nums)
            while l + 1 < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m
                else:
                    r = m
            return l     
        start = searchLeft(nums, target)
        end = searchRight(nums, target + 1)
        if end < start:
            return [-1, -1]
        return [start, end]
# @lc code=end

