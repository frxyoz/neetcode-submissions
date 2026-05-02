# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def trav(node, minVal, maxVal):
            if not node:
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False
            return trav(node.left, minVal, node.val) and trav(node.right, node.val, maxVal)
            
            


        return trav(root, float("-inf"), float("inf"))