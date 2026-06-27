class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        
        groups = n // groupSize
        hand = sorted(hand)
        counts = dict(Counter(hand))
        
        for _ in range(groups):
            start = hand[0]
            for i in hand:
                if counts[i] != 0:
                    start = i
                    break
            for x in range(start, start + groupSize):
                if counts.get(x, 0) == 0:
                    return False

            for x in range(start, start + groupSize):
                counts[x] -= 1

        return True