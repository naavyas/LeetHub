# Last updated: 3/25/2025, 8:29:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding the question: 
we keep going through the tress till we reach the leaf node 
we define a menthod that calculates the leaf sequences by recurisvely adding all the leaf nodes to a list 
then we call this method with both the trees and compare the lists that are returned 
if the lists are the same then we return true 
else return false 

recursive fn: 
base case that checks if the left and right == None then we append the value to the  list and return 
else we keep calling the left and keep calling the right 
the list is passed as a parameter of the function 
"""
class Solution:
    def findLeaf(self,n,leaves_of_tree1):
        if n.left == None and n.right == None:
            leaves_of_tree1.append(n.val)
            return 
        if n.left!=None:
            self.findLeaf(n.left,leaves_of_tree1)
        if n.right != None:
            self.findLeaf(n.right,leaves_of_tree1)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_seq1 = []
        leaf_seq2 = []
        self.findLeaf(root1,leaf_seq1)
        self.findLeaf(root2,leaf_seq2)
        if leaf_seq1 == leaf_seq2:
            return True
        else:
            return False

        
        