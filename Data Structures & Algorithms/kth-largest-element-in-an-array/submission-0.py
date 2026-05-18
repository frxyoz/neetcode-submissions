class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-x for x in nums]
        heapq.heapify(arr)
        while k > 1:
            heapq.heappop(arr)
            k -= 1
        return -1 * arr[0]
