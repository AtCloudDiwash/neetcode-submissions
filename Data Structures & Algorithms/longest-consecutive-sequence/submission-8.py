class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in store:
            
                length = 0

                while num + length in store:
                    length += 1
                res = max(res, length)
            else:
                continue
        return res
            

        