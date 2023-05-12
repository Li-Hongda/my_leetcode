#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum, max_avg = 0, -math.inf
        start = 0
        for end in range(len(nums)):
            sum += nums[end]
            if end - start == k-1:
                max_avg = max(max_avg, sum/k)

            if end-start >= k-1:
                sum -= nums[start]
                start += 1
            
        return max_avg
    

# @lc code=end

