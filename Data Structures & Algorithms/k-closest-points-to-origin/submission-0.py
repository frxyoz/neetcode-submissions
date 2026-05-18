class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for x in points:
            heapq.heappush(heap, (x[0]**2 + x[1]**2, [x[0], x[1]]))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
