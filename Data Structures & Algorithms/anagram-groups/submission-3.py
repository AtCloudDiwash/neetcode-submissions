class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = defaultdict(list)

        for item in strs:
            sortedS = "".join(sorted(item))
            store[sortedS].append(item)
        
        return [value for key, value in store.items()]
        