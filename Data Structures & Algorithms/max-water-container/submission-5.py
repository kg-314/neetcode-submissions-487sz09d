class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            area = (p2 - p1) * min(heights[p1], heights[p2])
            if area > maxArea:
                maxArea = area

            if heights[p2] < heights[p1]:
                p2 -= 1
            else:
                p1 += 1
        return maxArea
