# Last updated: 3/25/2025, 8:31:25 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
use the pointers to keep moving till they overlap. if they overlap then the linked list has a cycle
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        slow = head 
        fast = head 
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True 
        return False
        