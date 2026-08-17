class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        have = need = 0
        storeA = defaultdict(int)
        storeB = defaultdict(int)
        res = ""

        for c in t:
            storeA[c] += 1
            need += 1

        for r in range(len(s)):
            storeB[s[r]] += 1
            if s[r] in storeA and storeA[s[r]] >= storeB[s[r]]:
                have += 1
            while have >= need:
                if len(res) > len(s[l: r+1]) or res == "":
                    res = s[l: r+1]
                storeB[s[l]] -= 1
                if s[l] in storeA and storeA[s[l]] > storeB[s[l]]:
                    have -= 1
                l += 1
            
        return res


        