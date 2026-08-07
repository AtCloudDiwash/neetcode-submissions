class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] < (nums[i] * -1):
                        left += 1
                    elif nums[left] + nums[right] > (nums[i] * -1):
                        right -= 1
                    else:
                        res.append([nums[left], nums[right], nums[i]])
                        left += 1
                        right -= 1
        return res
                        
        


