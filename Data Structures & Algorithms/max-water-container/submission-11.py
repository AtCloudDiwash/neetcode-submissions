class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        highest = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)

            if heights[left] >= heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            
            highest = max(highest, area)

        return highest



