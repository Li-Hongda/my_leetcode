#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = math.inf
        start = 0
        sum_ = 0
        for end in range(len(nums)):
            sum_ += nums[end]
            if sum_ > target:
                minlen = min(minlen, end-start+1)
            
            while sum_ >= target:
                minlen  = min(minlen, end-start+1)
                sum_ -= nums[start]
                start += 1
        if minlen == math.inf:
            return 0
        else:
            return minlen

# @lc code=end

