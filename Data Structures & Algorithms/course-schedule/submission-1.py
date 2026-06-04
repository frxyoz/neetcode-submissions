class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        prereqs_dict = {i:[] for i in range(numCourses)}
        for prereq, req in prerequisites:
            prereqs_dict[prereq].append(req)
        
        path = set()

        def dfs(node):
            if node in path:
                return False
            path.add(node)
            
            for prereq in prereqs_dict[node]:
                if dfs(prereq) == False:
                    return False
            path.remove(node)
            return True

        for node in prereqs_dict:
            if dfs(node) == False:
                return False
        return True

            
                


                
                
                
            