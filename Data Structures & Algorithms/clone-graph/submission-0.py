"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]
            clones[node] = Node(node.val, None)
            if node.neighbors:
                neighbors = []
                for neighbor in node.neighbors:
                    neighbors.append(dfs(neighbor))
                clones[node].neighbors = neighbors
            return clones[node]

        return dfs(node)
            


        
        