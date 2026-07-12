class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True

        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                edges.append((abs(xj - xi) + abs(yj - yi), i, j))
        edges.sort()

        total = 0
        count = 0
        for weight, i, j in edges:
            if union(i, j):
                total += weight
                count += 1
                if count == n - 1:
                    break
        return total