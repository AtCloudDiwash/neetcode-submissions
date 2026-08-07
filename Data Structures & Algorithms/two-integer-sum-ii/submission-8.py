class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Search index for the element in the numbers that is just less than target
        highest = 0
        for i in range(len(numbers)):
            if numbers[i] >= target:
                highest = i - 1
                break
            highest = i

        leftPointer = 0
        rightPointer = highest

        while leftPointer < rightPointer:
            if numbers[rightPointer] + numbers[leftPointer] == target:
                break
            if numbers[rightPointer] + numbers[leftPointer] > target:
                leftPointer = 0
                rightPointer -= 1
            else:
                leftPointer += 1
        print(leftPointer, rightPointer)
        return list(sorted([leftPointer + 1, rightPointer + 1]))
        
        
                
        
