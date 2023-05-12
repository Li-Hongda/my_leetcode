#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = math.inf
        sum = 0
        start = 0
        for end in range(len(nums)):
            sum += nums[end]
            while sum >= target:
                minlen = min(minlen, end -start+1)
                sum -= nums[start]
                start += 1
        if minlen == math.inf:
            return 0
        else:
            return minlen


# @lc code=end

