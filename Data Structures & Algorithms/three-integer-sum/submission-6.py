class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        prevNum = sortedNums[0] -1
        res = []

        for i in range(len(sortedNums)):
            print(hit)
            if nums[i] == prevNum:
                continue
            else:
                left, right = i + 1, len(sortedNums) - 1
                while left < right:
                    if sortedNums[left] + sortedNums[right] < (nums[i] * -1):
                        left += 1
                    elif sortedNums[left] + sortedNums[right] > (nums[i] * -1):
                        right -= 1
                    else:
                        res.append([sortedNums[left], sortedNums[right], nums[i]])
                        break
            prevNum = nums[i]

        return res
                        
        


