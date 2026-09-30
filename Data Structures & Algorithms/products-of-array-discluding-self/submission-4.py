# We have a integer nums
# return an array output such that each index is the product
# of all other elements except itself
# We want to solve in O(n) time w/o using division

# Plan:
# 1. Use a prefix and suffix solution
# 2. First we iterate from left to right and store the prefix product 
# for each index in a prefix array excuding the current index number.
# 3. Then iterate from right to left and store the suffix product
# for each index 
#

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
           
        
        return output
        