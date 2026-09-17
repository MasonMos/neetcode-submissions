# Problem:
# 1. Given an array of numbers (nums) and integer (target)
# 2. Need to return indices i and j
# 3. Every input has exactly one pair of indices i and j

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i] 
            hashmap[nums[i]] = i

