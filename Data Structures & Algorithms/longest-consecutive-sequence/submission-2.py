class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numsMap = {}

        min = math.inf
        max = -math.inf

        for i in nums:
            numsMap[i] = numsMap.get(i, 0) + 1

            if i < min:
                min = i
            if i > max:
                max = i

        answer = 0
        
        counter = 0
        for i in range(min, max+1):
            temp = numsMap.get(i, 0)
            if temp == 0:
                counter = 0
            else:
                counter += 1
            if counter > answer:
                answer = counter
        return answer