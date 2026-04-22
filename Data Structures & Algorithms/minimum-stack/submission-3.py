class MinStack:

    def __init__(self):
        self.orderarr = []
        self.minarr = []

    def push(self, val: int) -> None:
        self.orderarr.append(val)
        if len(self.minarr) == 0:
            self.minarr.append(val)
        else:
            self.minarr.append(min(val, self.minarr[-1]))

    def pop(self) -> None:
        self.orderarr.pop()
        self.minarr.pop()

    def top(self) -> int:
        return self.orderarr[-1]

    def getMin(self) -> int:
        return self.minarr[-1]
