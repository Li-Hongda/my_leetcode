#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while 1:
            try:
                nums.remove(val)
            except:
                return len(nums)
# @lc code=end

