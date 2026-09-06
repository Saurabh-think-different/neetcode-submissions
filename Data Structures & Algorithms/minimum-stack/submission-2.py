class MinStack:
    import math
    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini:
            if val < self.mini[-1]:
                self.mini.append(val)
            else:
                self.mini.append(self.mini[-1])
        else:
            self.mini.append(val) 

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
