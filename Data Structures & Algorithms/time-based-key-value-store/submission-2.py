from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        else:
            l = 0
            r = len(self.d[key]) - 1
            values = self.d[key]
            res = ""
            while (l <= r):
                mid = (l + r )// 2
                
                if values[mid][0] <= timestamp:
                    res = values[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
            return res