#https://leetcode.com/problems/linked-list-random-node/editorial/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.n = 0
        p = head
        while p != None:
            p = p.next
            self.n += 1

    def getRandom(self) -> int:
        random_int = random.randint(0, self.n - 1)
        p = self.head
        while random_int:
            random_int -= 1
            p = p.next
        return p.val
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()