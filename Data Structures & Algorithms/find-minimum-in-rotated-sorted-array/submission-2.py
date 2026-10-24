'''
Know: 
- Given an array of length n.
- Originally sorted in ascending order. e.g (1,2,3)
- Must be rotated at least once
- All nums are unique
- Must return the minimum element in the array
- Not concerned about how many times the array is rotated
Plan:
- Use a binary search (recursion)
- We can start in the middle and check index-1 and index+1
- If index-1 is less than index, check the left side
- if index+1 is less than index, check the right side
- if index-1 is greater than index then return element[index]
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # we do this because we need to find out how many times
            # if we know that the bigger number is on the left,
            # then we know that the minimum is on the right side
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]