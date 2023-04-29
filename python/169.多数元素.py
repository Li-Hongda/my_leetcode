#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         major = 0
#         count = 0
        
#         for n in nums:
#             if count == 0:
#                 major = n
#             if n == major:
#                 count = count + 1
#             else:
#                 count = count - 1

#         return major
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return [k for k, v in Counter(nums).items() if v > len(nums) // 2]
# @lc code=end

