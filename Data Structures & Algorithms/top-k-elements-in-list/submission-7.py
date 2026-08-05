class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        
        sortedStore = sorted(store.keys(), key = store.get, reverse = True)
        return sortedStore[0: k]

