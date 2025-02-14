# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
how to invert the tree 
using a recursive approach 
4 - root remains the same

"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        
        temp = root.left 
        root.left = root.right 
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root





        