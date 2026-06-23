class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)

        if length == 1:
            return [0]
        result = [0] * length
        stack = []

        for i in range(length - 1, -1, -1):
            while stack:
                if stack[-1][0] > temperatures[i]:
                    result[i] = stack[-1][1] - i
                    break
                stack.pop()
            if not stack:
                result[i] = 0
            stack.append([temperatures[i], i])
        return result

