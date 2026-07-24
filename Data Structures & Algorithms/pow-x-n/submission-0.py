class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = x
        while n <= 0:
            res = res / x
            n += 1
        while n > 1:
            res *= x
            n -= 1
        return res