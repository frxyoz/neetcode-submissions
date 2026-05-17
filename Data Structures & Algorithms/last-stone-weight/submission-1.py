class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = [-x for x in stones]
        heapq.heapify(lst)
        while len(lst) >= 2:
            first, second = heapq.heappop(lst), heapq.heappop(lst)
            if first == second:
                continue
            heapq.heappush(lst, -1 * abs(first-second))
        return -1 * lst[0] if len(lst) > 0 else 0
