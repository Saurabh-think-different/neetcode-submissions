class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        char_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in char_dict:
                if not arr or arr.pop() != char_dict[i]:
                    return False
            else:
                arr.append(i)
        return len(arr) == 0