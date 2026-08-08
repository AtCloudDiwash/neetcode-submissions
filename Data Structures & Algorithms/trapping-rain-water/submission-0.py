class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        total = 0

        while left < right:
            if rightMax >= leftMax:
                left += 1
                leftMax = max(leftMax, height[left])
                total += leftMax - height[left]
            elif rightMax < leftMax:
                right -= 1
                rightMax = max(rightMax, height[right])
                total += rightMax - height[right]
        return total

            