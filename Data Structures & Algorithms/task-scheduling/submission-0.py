class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        q = []
        heap = []
        time = 1
        for task, freq in freqs.items():
            heapq.heappush(heap, (-freq, task))
        while heap or q:
            
            if q and q[0][0] == time:
                t, freq, v = q.pop(0) 
                heapq.heappush(heap, (freq, v))
            if heap:
                freq, v = heapq.heappop(heap)
                freq += 1
                if freq != 0:
                    q.append((time + n + 1, freq, v))
            time += 1
        return time - 1