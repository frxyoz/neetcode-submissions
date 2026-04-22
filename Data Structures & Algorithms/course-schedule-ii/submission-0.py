class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque

        prereqs = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
            
        visited, path = set(), set()
        order = []

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            
            path.add(node)
            for prereq in prereqs[node]:
                if not dfs(prereq):
                    return False
            path.remove(node)
            visited.add(node)
            order.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order





                

