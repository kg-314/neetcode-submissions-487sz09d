class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer method uses O(n) time and O(1) space.
        p1 = 0
        p2 = len(height) - 1

        leftMax = 0
        rightMax = 0

        sum = 0

        while p1 < p2:
            leftMax = max(leftMax, height[p1])
            rightMax = max(rightMax, height[p2])
            
            if leftMax < rightMax:
                sum += leftMax - height[p1]
                p1 += 1
            else:
                sum += rightMax - height[p2]
                p2 -= 1
        return sum