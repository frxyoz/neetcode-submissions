class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = [-x for x in nums]
        heapq.heapify(self.max_heap)
        self.k = k        

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)

        stk = []

        for i in range(self.k):
            stk.append(heapq.heappop(self.max_heap))

        ret = -stk[self.k - 1]

        for i in stk:
            heapq.heappush(self.max_heap, i)

        return ret