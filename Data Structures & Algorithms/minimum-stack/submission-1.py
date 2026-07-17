from collections import deque


class MinStack:
    def __init__(self):
        self.vals = deque()

    def push(self, val: int) -> None:
        self.vals.append(val)

    def pop(self) -> None:
        self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        l = []
        min_val = self.vals[-1]
        # find min
        while len(self.vals):
            min_val = min(min_val, self.vals[-1])
            l.append(self.vals.pop())
        # Repopualte stack
        while len(l):
            self.vals.append(l.pop())
        return min_val