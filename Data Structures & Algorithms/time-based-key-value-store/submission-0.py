class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        values = self.d[key]

        l = 0
        r = len(values) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            mid_timestamp = values[mid][1]
            mid_value = values[mid][0]

            if int(mid_timestamp) <= int(timestamp):
                # 当前结果满足条件，先保存
                result = mid_value

                # 继续往右找更大的合法 timestamp
                l = mid + 1
            else:
                # 当前 timestamp 太大
                r = mid - 1

        return result
        
