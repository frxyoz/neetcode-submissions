# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])

        i = 0
        while i < len(inorder) and inorder[i] != preorder[0]:
            i += 1
        leftInorder, rightInorder = inorder[:i], inorder[i+1:]

        leftPreorder = preorder[1 : 1 + len(leftInorder)]
        rightPreorder = preorder[1 + len(leftInorder) :]
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)

        return root