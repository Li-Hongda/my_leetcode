#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# 迭代法进行层序遍历
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []
    #     cur, res = [root], []
    #     while cur:
    #         lay, layval = [], []
    #         for node in cur:
    #             layval.append(node.val)
    #             if node.left: lay.append(node.left)
    #             if node.right: lay.append(node.right)
    #         cur = lay
    #         res.append(layval)
    #     return res
    
# 利用队列迭代进行遍历
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res



# @lc code=end

