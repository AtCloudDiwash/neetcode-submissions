class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        def isAlphaNum(s: str):
            if  ('A' <= s <= 'Z') or ('0' <= s <= '9'):
                return s
            else:
                return ""
        sanitized = "".join(list(filter(lambda x: isAlphaNum(x), s)))
        return sanitized[::-1] == sanitized 
        