#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
# 由于只能同时操作一只股票，假设第一天价格为A，第二天如果大于A就买，小于A就等第二天再买
# 如果连续大于对收益没有影响，（3-2）+（2-1）== 3-1、
# 如果连续小于 则一直等到最小值再买是收益最大的
# 如果起起伏伏，必须卖了前一支才能买。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
# @lc code=end

            
