class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connections = {i:[] for i in range(n)}
        for head, tail in edges:
            connections[head].append(tail)
            connections[tail].append(head)
        print(connections)
        
        visited, seen = set(), set()

        def dfs(node, parent):
            if node in visited:
                return False
            if node in seen:
                return True
            visited.add(node)
            for tail in connections[node]:
                if tail != parent:
                    if dfs(tail, node) == False:
                        return False
            visited.remove(node)
            seen.add(node)
            return True
        
        if dfs(0, -1) == False:
            return False
        return len(seen) == n
