#https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        self.head = head
        def rec(start,end):
            if start > end:
                return None
            m = (start + end) // 2
            
            left = rec(start, m - 1)
            node = TreeNode(val=self.head.val)
            self.head = self.head.next
            node.left = left
            node.right = rec(m + 1, end)
           
            return node
        return rec(0,n-1)