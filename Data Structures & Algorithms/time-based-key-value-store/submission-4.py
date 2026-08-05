class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        l = 0
        r = len(self.keys[key]) - 1
        vals = self.keys[key]

        if len(vals) == 0:
            return ""
        elif vals[l][0] > timestamp:
            return ""
        
        prev = ""

        while l <= r:
            m = ((r - l) // 2) + l
            ts = vals[m][0]

            if ts == timestamp:
                return vals[m][1]
            elif ts < timestamp:
                prev = vals[m][1]
                l = m + 1
            else:
                r = m - 1
        return prev