class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = defaultdict(int)
        l = 0
        res = 0

        for i in range(len(s)):

            store[s[i]] += 1

            while (i - l + 1) - max(store.values()) > k:
                store[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res

            

        