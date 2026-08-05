class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_arr = sorted(freq, key = freq.get, reverse=True)
        res = []

        for i in range(0, k):
            res.append(sorted_arr[i])

        return res
        