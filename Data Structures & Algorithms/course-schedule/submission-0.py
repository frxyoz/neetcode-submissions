class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        prereqs_dict = {i:[] for i in range(numCourses)}
        for prereq, req in prerequisites:
            prereqs_dict[prereq].append(req)
        
        path = set()

        def dfs(node):
            if node in path:
                return False
            if prereqs_dict[node] == []:   
                return True

            path.add(node)
            for prereq in prereqs_dict[node]:
                if not dfs(prereq):
                    return False
            path.remove(node)

            prereqs_dict[node] = []
            return True

        for x in range(numCourses):
            if not dfs(x):
                return False

        return True

            
                


                
                
                
            