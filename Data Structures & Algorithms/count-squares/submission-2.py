class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        for x, y in [point]:
            self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x, y = point
        for x1, y1 in self.points:
            if x1 == x:
                side = abs(y1 - y)
                if side:
                    if (x1+side, y1) in self.points and (x+side, y) in self.points:
                        count += (self.points[(x1, y1)] * self.points[(x1+side, y1)] * self.points[(x+side, y)])
                    if (x1-side, y1) in self.points and (x-side, y) in self.points:
                        count += (self.points[(x1, y1)] * self.points[(x1-side, y1)] * self.points[(x-side, y)])
        return count


