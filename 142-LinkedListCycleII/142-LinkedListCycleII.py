# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
we are given the head of the linked list 
we have to return the node where the cycle begins in the list 
cycle - if there is a node such that it can be reached by continously following the next pointer 
unclear on the wording of pos - will look at example to better understand 
eg: [3,2,0,-4] pos: 1
there is a cycle where the tail connects to the first node 
what we can do is we can keep moving through the linked list till we reach/find a value or address that has been traversed before
so as we go through the list we take the value we will be traversing 
DRY RUN :
temp = 2
prev = -4
addressed traveres = [3,2,0,-4]
lets think of a few edge cases:
looking at the constraints we know - 
there can be zero nodes in the list - in that case our code will return None
temp = head
        addresses_traversed = []
        if head == None:
            return None
        if head.next == None:
            return None
        # i need to have a prev 
        #prev = None
        while temp != None:
            if temp not in addresses_traversed: #check if the hash value of the node is in the array traversed 
                addresses_traversed.append(temp)
            else:
                return addresses_traversed[addresses_traversed.index(temp)]
            #prev = temp
            temp = temp.next
    
#temp will keep moving till it becomes none if there is no cycle and if there is a cycle then it will return gthe pos when it finds a loop. 
        return None

#Time complexiety : O(N) and space : O(N)

Thinking of an approach to optimize it in O(1) space :
to optimize in O(1) we have to use fast and slow pointers - when the fast and the slow pointers meet we know that there is a cycle 
        
#understanding this algo: we have a fast and slow pointer 
#the fast pointer moves twice as fast as the slow 
#when they meet u rest the slow to head and keep moving slow and fast by one step till they meet again 
#where they meet again is the initial pointer pos. 
"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next: #this moves ahead than slow
            slow = slow.next 
            fast = fast.next.next
            if slow == fast: #the pointers have met
                slow = head
                while slow!=fast:
                    slow = slow.next 
                    fast = fast.next#when they meet again you know where they started from and return that index
                return slow
        return None
        
      