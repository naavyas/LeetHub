# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []

        # Create a queue with root node and process until no more nodes in queue
        queue = [root]
        while queue:

        # Process the current number of nodes in queue to exclude new nodes added to queue. 
            levelCount = len(queue)
            level = []
            for i in range(levelCount):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

                # Store level into results.
            if level:
                results.append(level)

        # Return results.
        return results
    """
    def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
        h = height1(root)
        for i in range(1, h+1):
            printCurrLevel(root, i)
    
    def printCurrLevel(root, level):
        if root is None:
            return
        elif level == 1:
            print(root.val)
        else:
            printCurrLevel(root.left, level-1)
            printCurrLevel(root.right, level-1)
        
        
    def height1(root):
        if root is None:
            return 0
        else:
            lheight = height1(root.left)
            rheight - height1(root.right)
        if lheight>rheight: 
            return lheight + 1
        else:
            return rheight + 1
            
    """
