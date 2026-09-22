class Solution:
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return self.is_palindrome(s, L + 1, R) or self.is_palindrome(s, L, R - 1)
            L += 1
            R -= 1
        return True