class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k: int):
            hours = 0
            for i in piles:
                hours += math.ceil(i/k)
            return hours <= h


        maxVal = 0
        for i in piles:
            if i > maxVal:
                maxVal = i
        
        l, r = 1, maxVal
        while l < r:
            m = l + (r - l) // 2
            print(str(m))
            if check(m):
                r = m
            else:
                l = m + 1
       
        return l
            