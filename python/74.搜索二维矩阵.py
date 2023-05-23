#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for row in matrix:
            nums += row
        l = -1
        r = len(nums)
        exists = False
        while l + 1 != r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            elif nums[m] > target:
                r = m
            else: 
                exists = True
                break
        return exists
# @lc code=end

