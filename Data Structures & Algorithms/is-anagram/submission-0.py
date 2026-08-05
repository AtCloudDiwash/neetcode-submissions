class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setA = {}
        setB = {}

        for c in s:
            if c in setA:
                setA[c]+= 1
            else:
                setA[c] = 0
        
        for d in t:
            if d in setB:
                setB[d]+=1
            else:
                setB[d] = 0

        if setA == setB:
            return True
        else:
            return False
        