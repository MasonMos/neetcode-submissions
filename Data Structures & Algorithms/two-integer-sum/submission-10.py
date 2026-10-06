class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for num in range(len(nums)):
            diff = target - nums[num]
            if diff in hashmap:
                return [hashmap[diff], num]
            hashmap[nums[num]] = num
