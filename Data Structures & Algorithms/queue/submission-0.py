class Deque:
    
    def __init__(self):
        self.arr = []

    def isEmpty(self) -> bool:
        return len(self.arr) == 0

    def append(self, value: int) -> None:
        self.arr.append(value)

    def appendleft(self, value: int) -> None:
        self.arr.insert(0, value)

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr.pop()

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr.pop(0)
