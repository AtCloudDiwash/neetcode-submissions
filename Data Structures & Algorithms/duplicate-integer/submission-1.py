# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         dupli = {}

#         for item in nums:
#             if dupli.get(item, 0) != 0:
#                 return True
#             else:
#                 dupli[item] = 1
#         return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupli = set()

        for item in nums:
            if item in dupli:
                return True
            dupli.add(item)
        return False
        



    
        