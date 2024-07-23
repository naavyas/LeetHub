# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            nonlocal numMoves
            left=helper(node.left)
            right=helper(node.right)
            numMoves += abs(node.val+right+left-1)
            return node.val+right+left-1

        numMoves = 0
        helper(root)
        return numMoves
        