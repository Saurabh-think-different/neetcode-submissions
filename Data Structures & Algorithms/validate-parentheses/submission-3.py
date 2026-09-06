class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i, chr in enumerate(s):
            if chr == "(" or chr == "[" or chr == "{":
                arr.append(chr)
            if len(arr)==0 and (chr == ")" or chr == "]" or chr == "}"):
                return False
            elif chr == "}":
                if arr[-1] == "{":
                    arr.pop()
                else:
                    arr.append(chr)
            elif chr == "]":
                if arr[-1] == "[":
                    arr.pop()
                else:
                    arr.append(chr)
            elif chr == ")":
                if arr[-1] == "(":
                    arr.pop()
                else:
                    arr.append(chr)
        return len(arr) == 0