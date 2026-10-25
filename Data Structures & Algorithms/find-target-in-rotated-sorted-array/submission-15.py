'''
Know:
- Given an array of length n sorted in ascending order and target number
- It's been rotated between 1 and n times
- Need to find the target number in the array in O(log n) time
- Return the index or -1 if array isn't present
Plan:
- 


'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

                
        