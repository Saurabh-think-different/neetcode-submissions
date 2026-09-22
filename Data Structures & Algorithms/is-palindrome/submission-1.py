class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        L = 0
        R = len(s) - 1
        s = s.lower()
        s = [x for x in s if x.isalnum()]
        s = "".join(s)

        return s == s[::-1]
        # while L < R:
        #     if not s[R].isalnum():
        #         R -= 1
        #     if not s[L].isalnum():
        #         L += 1
        #     if not s[L] == s[R]:
        #         return False
        #     L += 1
        #     R -= 1
        # return True