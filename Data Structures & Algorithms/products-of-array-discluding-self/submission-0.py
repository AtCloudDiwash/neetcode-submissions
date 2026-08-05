class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     res = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             res *= nums[j]
        #     output.append(res)
        # return output

        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res = [0] * n

        prefix[0] = 1
        suffix[len(suffix) - 1] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]

        for k in range(len(res)):
            res[k] = prefix[k] * suffix[k]
        

        return res
