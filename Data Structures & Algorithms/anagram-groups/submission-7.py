class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        setStrs = set(["".join(sorted(i)) for i in strs])
        store = defaultdict(list)

        for item in strs:
            if "".join(sorted(item)) in setStrs:
                store["".join(sorted(item))].append(item)
        return list(store.values())

        

        