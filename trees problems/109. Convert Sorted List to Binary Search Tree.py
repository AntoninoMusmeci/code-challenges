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
    def sortedListToBSTSol2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        #recursion time: O(N) space O(log(N))
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

    def sortedListToBSTSol2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # create a tree backbone and balance the tree using rotations
        #time O(N) space: O(1)
        def compress(grand, m):
            node = grand.right
            while m > 1:
                m-=1
                old_node = node
                node = node.right
                grand.right = node
                old_node.right = node.left
                node.left = old_node
                grand = node
                node = node.right
        grand = TreeNode()
        node = grand 
        count = 0
        while head:
            node.right = TreeNode(head.val)
            head = head.next
            node = node.right
            count += 1
        height = int(log2(count+1))
        remaining_nodes = pow(2, height) - 1
        compress(grand, count-remaining_nodes)
        while remaining_nodes > 0:
            remaining_nodes /= 2
            compress(grand, remaining_nodes)
        return grand.right




