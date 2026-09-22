class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s = s.lower()
        s = [x for x in s if x.isalnum()]
        s = "".join(s)
        L = 0
        R = len(s) - 1

        while L < R:
            if not s[L] == s[R]:
                return False
            L += 1
            R -= 1
        return True