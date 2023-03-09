#https://leetcode.com/problems/linked-list-cycle-ii/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                break
        if fast== None or fast.next == None:
            return None
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow