class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedS = sorted(strs)
        store = defaultdict(list)

        for s in strs:
            store["".join(sorted(s))].append(s)
        return list(store.values())
