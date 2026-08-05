class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 0
        
        sortedStore = sorted(store.keys(), key = store.get, reverse = True)
        print(sortedStore)
        return sortedStore[0: k]

