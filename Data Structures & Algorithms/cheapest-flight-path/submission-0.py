class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            graph[from_i].append((to_i, price_i))
        distances = [float("inf")] * n
        distances[src] = 0

        heap = [(0, src, 0)]
        # best[node] = fewest stops used to reach it with the cost we accepted
        best_stops = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k:
                continue
            # only skip if we've already reached this node with <= stops (cheaper or equal path already explored)
            if node in best_stops and best_stops[node] <= stops:
                continue
            best_stops[node] = stops

            for to, price in graph[node]:
                heapq.heappush(heap, (cost + price, to, stops + 1))

        return -1