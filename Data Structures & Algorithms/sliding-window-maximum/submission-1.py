import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        arr = []
        
        for r in range(k):
            heapq.heappush(min_heap, (-nums[r], r))
        l, r = 0, k-1
        while r < len(nums):
            while min_heap[0][1] < l:
                heapq.heappop(min_heap)
            arr.append(-min_heap[0][0])
            l+=1
            r+=1
            if r != len(nums):
                heapq.heappush(min_heap, (-nums[r], r))
            
        return arr