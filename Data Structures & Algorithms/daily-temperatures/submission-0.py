class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        out = [0] * len(temperatures)
        for i in range(len(temperatures)):
            
            while stk and temperatures[i] > temperatures[stk[-1]]:
                out[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        return out