# Last updated: 5/23/2025, 7:39:09 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
the way we can reach of the  middle of the linked list is through 
iterating through the list using the pointers 
so we move fast faster than the next and it reaches the end first
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head 
        fast = head 
        if slow.next == None:
            return slow
        while fast and fast.next!=None:
            slow = slow.next 
            fast = fast.next.next 
        return slow 

        