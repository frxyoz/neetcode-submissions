class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        heap = [(0, k)]

        for ui, vi, ti in times:
            graph[ui].append((vi, ti))

        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distances[node]:
                continue
            for neighbor, w in graph[node]:
                if dist + w < distances[neighbor]:
                    heapq.heappush(heap, (dist + w, neighbor))
                    distances[neighbor] = min(distances[neighbor], dist + w)
        
        maxTime = 0
        for time in distances[1:]:
            if time == float('inf'):
                return -1
            maxTime = max(maxTime, time)
        return maxTime

            
        

            


