# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            lvllen = len(queue)
            lvl = []
            for i in range(lvllen):
                curr = queue.popleft()
                lvl.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(lvl[-1])
        
        return res
            

