class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = defaultdict(int)

        for num in nums:
            if num in store:
                return True
            
            store[num] = 1
        return False