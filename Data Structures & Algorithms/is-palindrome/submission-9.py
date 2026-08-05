class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def isAlphaNum(x):
            if 'a' <= x <= 'z' or '0' <= x <= '9':
                return True
            return False

        while left < right:
            while not isAlphaNum(s[left].lower()) and left < right:
                left += 1
            while not isAlphaNum(s[right].lower()) and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True