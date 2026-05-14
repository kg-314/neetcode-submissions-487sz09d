class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
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
                    if sublist not in result:
                        result.append(sublist)
                    p1 += 1
        return result