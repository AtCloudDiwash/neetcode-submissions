class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        storeA = [0]*26

        for i in range(len(s)):
            storeA[ord(s[i]) - ord('a')]+= 1
            storeA[ord(t[i]) - ord('a')]-= 1
        
        for item in storeA:
            if item != 0:
                return False
        return True
        
        