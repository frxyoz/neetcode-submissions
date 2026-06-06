
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        visited = set()
        res = 0
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        def dfs(node):
            visited.add(node)
            for v in adjList[node]:
                if v not in visited:
                    dfs(v)
            
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
        
        return res


        