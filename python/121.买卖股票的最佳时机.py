#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
# 暴力枚举法
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_diff = 0
#         for i in range(0, len(prices)):
#             for j in range(0, i):
#                 if prices[i] - prices[j] > max_diff:
#                     max_diff = prices[i] - prices[j]
#         return max_diff

# 由于只能是先买后卖，即利益为后面减前面，
# 所以相比于和之前出现过的所有值进行比较，只需比较最小值就行
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit



# @lc code=end

