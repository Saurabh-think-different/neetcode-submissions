class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i, op in enumerate(operations):
            if op == "+":
                arr.append(arr[-1]+arr[-2])
            elif op == "D":
                arr.append(arr[-1]*2)
            elif op == "C":
                arr.pop()
            else:
                arr.append(int(op))
        return sum(arr)