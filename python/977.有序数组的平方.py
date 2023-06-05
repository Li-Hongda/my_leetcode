#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # new = []
        # l = 0
        # r = len(nums) - 1
        # while l <= r:
        #     left = pow(nums[l], 2)
        #     right = pow(nums[r], 2)
        #     if left > right:
        #         new.append(left)
        #         l += 1
        #     else:
        #         new.append(right)
        #         r -= 1
        # return new[::-1]
        new = [pow(a, 2) for a in nums]
        return sorted(new)
# @lc code=end  

