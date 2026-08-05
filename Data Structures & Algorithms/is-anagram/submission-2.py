class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        storeA = {}
        storeB = {}


        for c in s:
            if c in storeA:
                storeA[c] += 1
            else:
                storeA[c] = 1
        for c in t:
            if c in storeB:
                storeB[c] += 1
            else:
                storeB[c] = 1
        
        for c in storeA:
            if (c not in storeB) or (storeA[c] != storeB[c]):
                return False
        return True


