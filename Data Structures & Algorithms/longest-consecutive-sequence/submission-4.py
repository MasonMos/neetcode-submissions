class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestCount = 0

        for num in nums:
            length = 0
            if (num - 1) not in numSet:
                length += 1
                while num + length in numSet:
                    length += 1        
                longestCount = max(longestCount, length)
        return longestCount