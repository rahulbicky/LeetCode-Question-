class MinStack:

    def __init__(self):
        self.items = []

    def push(self, value: int) -> None:
        if len(self.items) == 0:
            self.items.append([value, value])
        else:
            mini = min(self.items[-1][1], value)
            self.items.append([value, mini])

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]