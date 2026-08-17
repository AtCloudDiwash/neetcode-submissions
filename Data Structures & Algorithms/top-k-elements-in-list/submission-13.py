class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]
        res = []

        for num in nums:
            store[num] += 1
        
        for key, value in store.items():
            freq[value].append(key)

        for i in range(len(freq) - 1, -1, -1):
            for f in freq[i]:
                res.append(f)
            if len(res) == k:
                return res
        return res

        

        