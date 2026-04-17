class Solution:
    def findMin(self, nums: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(nums) - 1
        # if leftPtr is less than mid, and rightPtr is also less than mid,
        # then i know that the minimum is to the right of mid.

        # if leftPtr is greater than mid, and rightPtr is greater than mid,
        # then I know that the minimum is to the left of mid.

        # I want to get leftPtr to be the max value, and rightPtr to be the 
        # value just before min.

        while leftPtr < rightPtr:
            mid = leftPtr + (rightPtr - leftPtr) // 2
            if nums[mid] < nums[rightPtr]:
                rightPtr = mid
            else:
                leftPtr = mid + 1
        return nums[leftPtr]



            
        