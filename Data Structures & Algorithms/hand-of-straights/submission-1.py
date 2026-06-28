class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        
        counts = defaultdict(int)
        for x in hand:
            counts[x] += 1
        smallestList = list(counts.keys())
        heapq.heapify(smallestList)

        while smallestList:
            start = smallestList[0]
            for i in range(start, start + groupSize):
                print(i)
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if smallestList[0] != i:
                        return False
                    heapq.heappop(smallestList)
        
        return True