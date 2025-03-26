# Last updated: 3/25/2025, 11:45:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == val:
            return root
        if root.left!=None:
            b = self.searchBST(root.left,val)
            if b!=None:
                return b
        if root.right!=None:
            b = self.searchBST(root.right,val)
            if b!=None:
                return b
        return None
        
        



        