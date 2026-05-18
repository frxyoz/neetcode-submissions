import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = dict(Counter(nums))
        heap = []
        ans = []
        for value, freq in freqs.items():
            heapq.heappush(heap, (freq, value))
            if len(heap) > k:
                heapq.heappop(heap)
        for freq, value in heap:
            ans.append(value)
        return ans

        
        
