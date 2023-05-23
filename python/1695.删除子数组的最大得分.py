#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxscore = 0
        start=0
        a = dict()
        sum_ = 0
        for end in range(len(nums)):
            sum_ += nums[end]
            a[nums[end]] = a.get(nums[end], 0) + 1
            if end - start + 1 == len(a):
                maxscore = max(maxscore, sum_)
            while end - start + 1 > len(a):
                head = nums[start]
                a[head] -= 1
                sum_ -= head
                if a[head] == 0:
                    del a[head]                
                start += 1

        return maxscore

# @lc code=end

