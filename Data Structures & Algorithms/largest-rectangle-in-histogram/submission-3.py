class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        rightMost = [len(heights)]*len(heights)
        leftMost = [-1]*len(heights)

        # Find the rightmost bar for ith height
        for i in range(len(heights) - 1, -1, -1):

            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if stack:
                rightMost[i] = stack[-1]
            
            stack.append(i)

        stack.clear()

        # Find the leftmost bar for ith bar
        for i in range(len(heights)):

            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if stack:
                leftMost[i] = stack[-1]
            
            stack.append(i)

        # Find the area
        area = 0
        for i in range(len(heights)):
            area = max(area, (rightMost[i] - leftMost[i] - 1) * heights[i])
        return area


        #monotonic stack solution

        