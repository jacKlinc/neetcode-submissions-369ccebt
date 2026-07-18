from collections import deque


class MyStack:
    def __init__(self):
        self.vals = deque()

    def push(self, x: int) -> None:
        self.vals.append(x)

    def pop(self) -> int:
        for i in range(len(self.vals) - 1):
            self.push(self.vals.popleft())
        # return the last value
        return self.vals.popleft()


    def top(self) -> int:
        return self.vals[-1]

    def empty(self) -> bool:
        return not self.vals
