class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        storeA = [0] * 26
        storeB = [0] * 26

        for i in range(len(s1)):
            storeA[ord(s1[i]) - ord('a')] += 1

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                storeB[ord(s2[l]) - ord('a')] -= 1
                l += 1
            storeB[ord(s2[r]) - ord('a')] += 1
            if storeB == storeA:
                return True
        return False


        