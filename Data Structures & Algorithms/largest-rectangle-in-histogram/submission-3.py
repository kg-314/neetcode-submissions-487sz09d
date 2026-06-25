class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        # Go from left to right finding the bar that limits current bar.
        # We can freely pop bars that do no limit current bar b/c
        # current bar would become the limiter for another bar after it that
        # that is higher.
        stack = []
        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        # Same idea but right to left
        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        maxArea = 0
        for i in range(n):
            height = heights[i]
            width = (rightMost[i] - 1) - (leftMost[i] + 1) + 1
            maxArea = max(maxArea, width * height)
        return maxArea
