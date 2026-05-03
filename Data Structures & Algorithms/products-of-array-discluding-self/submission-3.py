class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_counter = 0

        for i in nums:
            if i != 0:
                product *= i
            else:
                zero_counter += 1
        

        products = []

        for i in range(0, len(nums)):
            if zero_counter > 0:
                if nums[i] != 0:
                    products.append(0)
                elif zero_counter > 1: 
                    products.append(0)
                else:
                    products.append(product)
            else:
                products.append(product//nums[i])
        return products