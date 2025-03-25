# Last updated: 3/25/2025, 12:00:32 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #dry run: [1,2,3,4,5] // even no of nodes
        #[1]
        #slow = 3
        #fast = 5
        if head.next == None:
            return head
        slow = head 
        fast = head 
        while fast != None and fast.next != None :
            slow = slow.next 
            fast = fast.next.next 
        return slow 

        