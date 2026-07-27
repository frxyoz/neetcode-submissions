class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        # what
        while n != 1 and n not in seen:
            seen.add(n)
            newnum = 0
            while n > 0:
                newnum += (n % 10) ** 2
                n = n // 10
            n = newnum
        return n == 1