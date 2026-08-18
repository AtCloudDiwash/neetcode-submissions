class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        store = [0] * 26

        for c in s:
            store[ord(c) - ord('a')] += 1
        for c in t:
            store[ord(c) - ord('a')] -= 1

        for item in store:
            if item != 0:
                return False
        return True
            
        