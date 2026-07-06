class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i = 0
        q = []
        res = [-1] * len(queries)
        heap = []
        for index, value in enumerate(queries):
            q.append((value, index))
        q.sort()
        for query, index in q:
            while i < len(intervals) and intervals[i][0] <= query: 
                heapq.heappush(heap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i += 1
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            if heap:
                res[index] = heap[0][0]

        return res

