class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Search index for the element in the numbers that is just less than target
        highest = 0
        for i in range(len(numbers)):
            if numbers[i] >= target:
                highest = i - 1
                break

        leftPointer = 0
        rightPointer = highest

        while leftPointer < rightPointer:
            if numbers[rightPointer] + numbers[leftPointer] == target:
                return [numbers[leftPointer], numbers[rightPointer]]
            if numbers[rightPointer] + numbers[leftPointer] > target:
                leftPointer = 0
                rightPointer -= 1
        
                
        
