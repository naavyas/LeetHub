# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
understanding the question: 
we are given the head of a linked list and we remove the nth node from the end of the list and return its head
Ideas: 
go through the whole list and find out the number of elements that could be present 
then subract that - n . reach that number and then delete the next element
if there is only one element in the list then just remove that
ALTERNATIVE stack appraoch : 
go through the list and keep adding the elements to a stack 

"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #first iterate and find out how many elements are present in the list 
        temp = head
        num_nodes = 0 
        while temp!=None:
            num_nodes += 1
            temp = temp.next 
        node_to_delete = num_nodes - n 
        ctr = 0
        if num_nodes < n:
            return None
        if node_to_delete == 0:
            head = head.next
        else:
            temp = head
            while temp != None:
                ctr+=1
                if ctr == node_to_delete :
                    to_delete = temp.next
                    temp.next = to_delete.next
                    break
                temp = temp.next
        return head


        