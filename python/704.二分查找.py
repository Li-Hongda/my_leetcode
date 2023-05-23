#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        if target not in nums:
            return -1
        while l + 1 != r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m 
        return r
# @lc code=end

