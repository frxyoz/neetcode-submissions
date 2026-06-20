"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        
        q = deque()
        if root: q.append(root)

        while q:
            lenQ = len(q)
            for i in range(lenQ):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    q.append(curr.right)
                if i < lenQ - 1:
                    curr.next = q[0]
        return root
                    
                    