class TimeMap:

    def __init__(self):
        self.mpp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mpp:
            self.mpp[key] = [(timestamp, value)]
        else:
            self.mpp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mpp:
            return ""
        else:
            values = self.mpp[key]
            res = ""

            l, r = 0, len(values) - 1
            while l<= r:
                mid = (l + r) // 2

                if values[mid][0] <= timestamp:
                    res = values[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1

            return res

