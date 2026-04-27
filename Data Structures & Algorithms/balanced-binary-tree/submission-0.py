# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal = True

        def dfs(root):
            nonlocal isBal
            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            
            if abs(leftHeight - rightHeight) > 1:
                isBal = False

            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return isBal
