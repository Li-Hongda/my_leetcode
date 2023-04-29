#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         minprice = float('inf')
#         maxprofit = 0
#         for price in prices:
#             minprice = min(minprice, price)
#             maxprofit = max(maxprofit, price - minprice)
#         return maxprofit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

# @lc code=end

