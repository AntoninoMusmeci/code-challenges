#https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoList(l1,l2):
            head = p = ListNode()
            while l1 != None and l2!= None:
                if l1.val <= l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            if l1 != None:
                p.next = l1
            if l2 != None:
                p.next = l2
            return head.next


        n = len(lists)
        not_selected = 1
        while not_selected < n:
            i = 0
            for i in range(0,n-not_selected, not_selected*2):
                lists[i] = mergeTwoList(lists[i],lists[i + not_selected])
            not_selected *= 2
        return lists[0] if n > 0 else None