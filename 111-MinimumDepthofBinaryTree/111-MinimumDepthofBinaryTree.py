# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
basic revision of bfs - breadth first search
have a queue and keep adding the elements per level of the tree 
we can have a pointer that helps keep track of the length of the tree
 def dfs(root,len):
        if root == None:
            return 
        if root.left == None and root.right == None:
            return len
        else:
            if root.left!=None:
                l = self.dfs(root.left, len+1)
            if root.right!=None:
                r = self.dfs(root.right,len+1)
        if l<=r:
            return l
        else:
            return r
"""
class Solution:
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append(root)
        ctr = 0
        if root == None:
            return 0
        while len(queue) != 0:
            l = len(queue)
            ctr += 1
            for r in range(l):
                #print(queue)
                var = queue.pop(0)
                if var.left == None and var.right == None:
                    return ctr
                if var.left!=None:
                    queue.append(var.left)
                if var.right!=None:
                    queue.append(var.right)
        return ctr
        
        