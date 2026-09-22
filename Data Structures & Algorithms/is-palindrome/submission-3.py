class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c
        L = 0
        R = len(new_s) - 1

        while L < R:
            if not new_s[L] == new_s[R]:
                return False
            L += 1
            R -= 1
        return True