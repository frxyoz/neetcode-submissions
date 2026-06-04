class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        pq, aq = deque(), deque()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pac.add((r, c))
                    pq.append((r, c))
                if r == ROWS - 1 or c == COLS - 1:
                    atl.add((r, c))
                    aq.append((r, c))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while pq:
            r, c = pq.popleft()
            for dr, dc in directions:
                if min(r + dr, c + dc) < 0 or r + dr >= ROWS or c + dc >= COLS:
                    continue
                if (r + dr, c + dc) in pac:
                    continue
                if heights[r + dr][c + dc] >= heights[r][c]:
                    pac.add((r+dr, c+dc))
                    pq.append((r+dr, c+dc))
        while aq:
            r, c = aq.popleft()
            for dr, dc in directions:
                if min(r + dr, c + dc) < 0 or r + dr >= ROWS or c + dc >= COLS:
                    continue
                if (r + dr, c + dc) in atl:
                    continue
                if heights[r + dr][c + dc] >= heights[r][c]:
                    atl.add((r+dr, c+dc))
                    aq.append((r+dr, c+dc))
        
        res = []
        for r, c in pac & atl:
            res.append([r, c])
        return res