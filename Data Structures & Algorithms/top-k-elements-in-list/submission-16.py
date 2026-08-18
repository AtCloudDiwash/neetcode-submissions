class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = [[] for _ in range(len(nums) + 1)]
        freq = defaultdict(int)
        res = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for key, value in freq.items():
            store[value].append(key)
        
        for i in range(len(store) - 1, -1, -1):
            for j in range(len(store[i])):
                if len(res) == k:
                    return res
                res.append(store[i][j])
        return res
            
            
