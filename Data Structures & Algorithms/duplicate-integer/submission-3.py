class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dupli = {}

        for num in nums:
            if num in dupli:
                return True
            else:
                dupli[num] = 1
        return False

