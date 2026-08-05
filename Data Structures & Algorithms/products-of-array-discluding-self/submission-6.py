class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        total = 1
        zeroNum = 0
        # check if num in nums have more than one zero

        for num in nums: 
            if num == 0:
                zeroNum += 1

        if zeroNum > 1:
            return [0]*len(nums)
        

        for num in nums:
            if num != 0:
                total *= num

        if zeroNum == 1:
            for i in range(0, len(nums)):
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = total
        else:
            for i in range(0, len(nums)):
                res[i] = total // nums[i]
        return res
        


        
        

                

             