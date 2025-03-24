# Last updated: 3/24/2025, 1:43:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self,root,subRoot):
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val != subRoot.val:
            return False 
        b1 = self.isSame(root.left, subRoot.left)
        if b1 == False:
            return False
        
        b2 = self.isSame(root.right,subRoot.right)
        if b2 == False:
            return False
        return True
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val == subRoot.val:
            n = self.isSame(root,subRoot)
        
            if n == True:
                return True 
    
        n = self.isSubtree(root.left,subRoot)
        if n:
            return True 
        m = self.isSubtree(root.right,subRoot)
        if m:
            return True
        
        
        return False


        