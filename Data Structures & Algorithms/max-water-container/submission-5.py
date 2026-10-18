# Know:
# We have int array [heights]
# heights[i] = height of ith bar
# Need to return the maximum amount of water a container can store
# 
# Approach:
# Use sliding window solution.
# Need to find the area every iteration
# Two pointers, one iterates through all heights
# Another will iterate ahead of the first one
# 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(heights) - 1

        while (i < j):
            width = j - i
            if (heights[i] < heights[j]):
                area = heights[i] * width
                maxArea = max(maxArea, area)
                i += 1
            else:
                area = heights[j] * width
                maxArea = max(maxArea, area)
                j -= 1
        
        return maxArea
                


        