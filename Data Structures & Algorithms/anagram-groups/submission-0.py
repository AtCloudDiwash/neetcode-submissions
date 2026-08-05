class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final_map = defaultdict(list)
        for item in strs:
            sortedItem = ''.join(sorted(item))
            final_map[sortedItem].append(item)
        print(final_map)
        print(final_map.values())
        return list(final_map.values())

