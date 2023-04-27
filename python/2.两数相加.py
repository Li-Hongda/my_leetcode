#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode(0)
        print(a)
        b = a
        carry = 0
        while l1 and l2:
            b.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            b = b.next
        while l1:
            b.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            b = b.next            
        while l2:
            b.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            b = b.next
        if carry == 1:
            b.next = ListNode(1)
        return a.next

# @lc code=end

