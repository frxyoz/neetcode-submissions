class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append([position[i], speed[i]])
        arr = (sorted(arr, reverse=True))
        stk = []
        for x, y in arr:
            time = (target - x) / y
            if (not stk) or (stk and time > stk[-1]):
                stk.append(time)
        return len(stk)

            