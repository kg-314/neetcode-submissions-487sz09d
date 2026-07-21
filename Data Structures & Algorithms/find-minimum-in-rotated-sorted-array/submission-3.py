class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] <= nums[r]:
            return nums[l]

        while l < r:
            m = (l + r) // 2 # DO NOT FORGET OPERATOR PRECEDENCE

            if nums[m] > nums[l]:
                # the pivot is to the right of m
                l = m
            elif nums[m] < nums[l]:
                # the pivot is to the left of m
                r = m
            else:
                # m == l: meaning we found the pivot
                l = r
                break
        
        return nums[l]