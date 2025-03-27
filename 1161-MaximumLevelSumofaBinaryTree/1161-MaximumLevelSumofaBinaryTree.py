# Last updated: 3/26/2025, 8:44:17 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
given the root of a binary tree 
level of the root is 1 
children satrt from level 2

return the smallest level such that the sum of the elements on that level is the max
"""
class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = []
        if root == None:
            return 0 
        queue.append(root) #[1]
        max_sum = -10 ** 5
        ctr = 0
        max_level = 0
        while len(queue) != 0:
            l = len(queue) # 2
            sum_level = 0
            ctr+=1 #2
            for r in range(l):
                var = queue.pop(0)
                sum_level += var.val #7
                if var.left != None:
                    queue.append(var.left) #[7,-8]
                if var.right != None:
                    queue.append(var.right)
            if sum_level>max_sum:
                max_sum = sum_level
                max_level = ctr #2
        return max_level
            


        