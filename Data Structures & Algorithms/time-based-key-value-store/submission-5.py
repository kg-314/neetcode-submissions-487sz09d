class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        vals = self.keys.get(key, [])

        l = 0
        r = len(vals) - 1

        while l <= r:
            m = ((r - l) // 2) + l

            ts = vals[m][0]

            if ts <= timestamp:
                ans = vals[m][1]
                l = m + 1
            else:
                r = m - 1
        return ans