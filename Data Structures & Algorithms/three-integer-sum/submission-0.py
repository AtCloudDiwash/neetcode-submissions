class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) * -1 in nums[j+1: len(nums)]:
                    if sorted([nums[i], nums[j], (nums[i] + nums[j]) * -1]) not in res:
                        res.append([nums[i], nums[j], (nums[i] + nums[j]) * -1])
        return res
        
        
