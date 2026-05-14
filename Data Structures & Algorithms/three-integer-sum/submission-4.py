class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:
                sum = nums[i] + nums[p1] + nums[p2]
                if sum < 0:
                    p1 += 1
                elif sum > 0:
                    p2 -= 1
                else:
                    sublist = [nums[i], nums[p1], nums[p2]]
                    result.append(sublist)
                    p1 += 1
                    p2 -= 1
                    while nums[p1] == nums[p1 - 1] and p1 < p2:
                        p1 += 1
        return result