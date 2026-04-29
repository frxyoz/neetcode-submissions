from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ret = []

        def bfs(node):
            queue = deque([(node, 0)])

            while queue:
                curr, lvl = queue.popleft()
                if len(ret) <= lvl:
                    ret.append([])
                ret[lvl].append(curr.val)

                if curr.left:
                    queue.append((curr.left, lvl+1))
                if curr.right:
                    queue.append((curr.right, lvl+1))

        bfs(root)
        return ret



        