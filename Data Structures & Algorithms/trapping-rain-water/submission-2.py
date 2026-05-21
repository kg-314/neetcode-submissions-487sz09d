class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix and suffix array soln is O(n) time, but also O(n) space.
        maxLeft = 0
        maxRight = 0

        diffLeft = [0] * len(height)
        diffRight = [0] * len(height)

        for i in range(0, len(height)):
            maxLeft = max(maxLeft, height[i])
            diffLeft[i] = maxLeft - height[i]
        
        for i in range(len(height) - 1, -1, -1):
            maxRight = max(maxRight, height[i])
            diffRight[i] = maxRight - height[i]

        # Find the smaller of the two enclosing walls for each water spot.

        sum = 0
        for i in range(0, len(diffLeft)):
            sum += min(diffLeft[i], diffRight[i])
        return sum