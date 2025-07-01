# Last updated: 7/1/2025, 4:04:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        right_side = []
        vals = []
        if not root: 
            return []
        right_side.append(root.val)
        queue.append(root)
        while len(queue)!= 0:
            l = len(queue)
            for _ in range(l): 
                var = queue.pop(0)
                if var.left!=None: 
                    queue.append(var.left)
                    vals.append(var.left.val)
                if var.right!=None: 
                    queue.append(var.right)
                    vals.append(var.right.val)
            if len(queue)!=0:
                right_side.append(vals[-1])
        return right_side
            


        