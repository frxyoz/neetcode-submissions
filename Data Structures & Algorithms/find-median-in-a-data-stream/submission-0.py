class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []


    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -1 * self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -1 * num)
        else:
            heapq.heappush(self.minHeap, num)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            maxLeft = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, maxLeft)
        elif len(self.maxHeap) < len(self.minHeap):
            minRight = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * minRight)

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return ((-1 * self.maxHeap[0]) + self.minHeap[0])/2
        else:
            return -1 * self.maxHeap[0]
        
        