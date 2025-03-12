# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1->2->1->2
2->1->2->1
as i go forward i put it in a stack : [2,1,2,1]
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head #store the head of a singly linked list 
        #return true if its is a palindrome and false otherwise
        if head.next == None:
            return True 
        forward = ''
        backward = ''
        stack = []
        while temp!=None:
            forward = forward + str(temp.val)
            stack.append(str(temp.val))
            temp = temp.next 
        while len(stack)!=0:
            backward = backward + stack.pop()
        if backward == forward: 
            return True
        else:
            return False

        
        
        



        