class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = set(nums)
        highest = 0
        for num in nums:
            if num - 1 not in newNums:
                length = 0
                while num + length in newNums:
                    length += 1
                highest = max(highest, length)
        return highest