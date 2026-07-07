class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        connections = defaultdict(list)
        res = []
        for dept, arr in tickets:
            connections[dept].append(arr)
        for src in connections:
            connections[src].sort(reverse=True)
        
        def dfs(airport):
            while connections[airport]:
                next = connections[airport].pop()
                dfs(next)
            res.append(airport)
        dfs("JFK")

        return res[::-1]