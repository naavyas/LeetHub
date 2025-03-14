# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
the numbers are stored in the linked list in reverse order 
each node contains a single digit 
add the 2 numbers and store the solution in a linked list 
2 numbers don't contain any leading zeros except the number 0 itself 
we have to go through both the linked lists and add each number 
maybe we should have a seperate linked list that stores and returns the sum
suppose its : 
2 -> 4 -> 5 
1 -> 6 -> 7 
output : 3 -> 0 -> 3 -> 1

"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 0
        head = ListNode(0)
        current = head
        while p1!=None and p2!=None:
            sum_val = p1.val + p2.val + carry 
            if sum_val > 9:
                carry = sum_val // 10 
                sum_val = sum_val % 10
            else:
                carry = 0
            newNode = ListNode(sum_val)
            p1 = p1.next 
            p2 = p2.next 
            current.next = newNode
            current = current.next 
        while p1!=None: 
            sum_val = carry + p1.val
            if sum_val<9:
                current.next = ListNode(sum_val)
                current = current.next 
                current.next = p1.next
                carry = 0 
                break
            else:
                carry = sum_val // 10
                sum_val = sum_val % 10
                current.next = ListNode(sum_val)
                current = current.next
                p1 = p1.next
        while p2!=None:
            sum_val = carry + p2.val
            if sum_val<9:
                current.next = ListNode(sum_val)
                current = current.next 
                current.next = p2.next
                carry = 0 
                break
            else:
                carry = sum_val // 10
                sum_val = sum_val % 10
                current.next = ListNode(sum_val)
                current = current.next
                p2 = p2.next
        if carry != 0:
            current.next = ListNode(carry)
            current = current.next
        return head.next






        