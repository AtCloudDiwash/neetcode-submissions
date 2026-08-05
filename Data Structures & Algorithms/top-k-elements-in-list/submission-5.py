class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)

        for num in nums:
            store[num] += 1
        
        sortedStore = sorted(store.items(), key = lambda x:x[1], reverse = True)
        res = []
        i = 0
        for item in sortedStore:
            if i  == k:
                return res
            res.append(item[0])
            i += 1
        return res