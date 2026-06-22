class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []

        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        res = ""

        for time, value in self.data[key]:
            if time <= timestamp:
                res = value
            else:
                break

        return res