class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        l = 0
        res = 0


        for i in range(len(s)):

            if s[i] in store:
                l = max(store[s[i]] + 1, l)
            store[s[i]] = i
            res = max(res, i - l +1)
        return res