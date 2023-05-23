#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True
        
        q = [(root.left,root.right)]
        while q:
            left, right = q.pop(0)

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False
            
            q.append((left.left,right.right))
            q.append((left.right,right.left))
        return True



# @lc code=end

