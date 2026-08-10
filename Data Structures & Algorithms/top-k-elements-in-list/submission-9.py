class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for _ in range(len(nums) + 1)]
        store = defaultdict(int)
        res = []
        count = 0

        for num in nums:
            store[num] += 1
        
        for key, value in store.items():
            freq[value].append(key)
        
        
        for i in range(len(freq) - 1, -1, -1):
            for j in range(0, len(freq[i])):
                if count == k:
                    return res
                res.append(freq[i][j])
                count += 1
        return res
