class TimeMap:
    def __init__(self):
        self.dih = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dih[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.dih[key]:
            return ""
        else:
            l, r = 0, len(self.dih[key])-1
            while l <= r:
                m = l + (r - l) // 2
                if self.dih[key][m][1] == timestamp:
                    return self.dih[key][m][0]
                elif self.dih[key][m][1] < timestamp:
                    l = m + 1
                else:
                    r = m - 1
            if r == -1:
                return ""
            return str(self.dih[key][r][0])
