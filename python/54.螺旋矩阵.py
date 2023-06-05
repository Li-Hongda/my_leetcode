#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)  # 取矩阵第一行并删除
            matrix = list(zip(*matrix))[::-1]  # 旋转矩阵
        return result

# @lc code=end

