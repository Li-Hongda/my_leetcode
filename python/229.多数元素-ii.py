#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 多数元素 II
#

# @lc code=start
# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         d = dict()        
#         for num in nums:
#             if num not in d:
#                 d[num] = 1
#             else:
#                 d[num] += 1
#         l = []
#         for k,v in d.items():
#             if v > len(nums) // 3:
#                 l.append(k)
#         return l

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v > len(nums) // 3]

# @lc code=end

