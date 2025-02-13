"""
def preOrder(self,node, l):
        if node == None:
            return
        self.preOrder(node.left,l)
        l.append(node.val)
        print(l)
        self.preOrder(node.right,l)
        

list_p = []
        list_q = []
        self.preOrder(p,list_p)
        self.preOrder(q,list_q)
        print('after calling both functions: ')
        print('p: ', list_p)
        print('q: ', list_q)
        if list_p == list_q:
            return True
        else:
            return False
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        if l == False or r == False:
            return False
        else:
            return True 
        


        