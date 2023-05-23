#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            leftHeight = maxDepth(root.left)
            rightHeight = maxDepth(root.right)
            return max(leftHeight, rightHeight) + 1
        left = maxDepth(root.left)
        right = maxDepth(root.right)
        return left + right
# @lc code=end

