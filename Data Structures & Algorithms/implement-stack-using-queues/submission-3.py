from collections import deque


class MyStack:
    def __init__(self):
        self.vals = deque()

    def push(self, x: int) -> None:
        self.vals.appendleft(x)

    def pop(self) -> int:
        return self.vals.popleft()

    def top(self) -> int:
        # this is wrong (should be getting the biggest val)
        return self.vals[0]

    def empty(self) -> bool:
        return not self.vals