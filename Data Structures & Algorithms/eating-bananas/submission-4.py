class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        bestRate = float('inf')

        

        while l <= r:
            m = (l + r) // 2

            totalHours = 0
            for pile in piles:
                hours = pile // m

                if pile % m > 0:
                    hours += 1
                totalHours += hours
            if totalHours > h:
                l = m + 1
            else:
                if m < bestRate:
                    bestRate = m
                r = m - 1
        return bestRate

