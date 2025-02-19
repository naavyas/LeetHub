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
        l = self.isSame(root.left, subRoot.left)
        r = self.isSame(root.right, subRoot.right)
        #print('l=', l, 'at', root.left)
        #print('r =', r, 'at', root.right)
        if r == False or l == False:
            #print('came')
            return False  
        else:
            return True

        
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if self.isSame(root,subRoot): 
            #print('yes')
            return True
        else:
            l = self.isSubtree(root.left, subRoot) 
            r = self.isSubtree(root.right,subRoot)
            if l == True or r == True:
                return True
            else: 
                return False
        
        
        