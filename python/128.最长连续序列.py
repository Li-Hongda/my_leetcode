#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 1
        tmplen = 1
        new_nums = sorted(set(nums))
        l = len(new_nums)
        if l == 0:
            return 0
        for i,num in enumerate(new_nums):
            if i < l - 1:
                if num + 1 == new_nums[i+1]:
                    tmplen += 1
                    maxlen = max(tmplen, maxlen)
                else:
                    tmplen = 1
        return maxlen   

# @lc code=end

