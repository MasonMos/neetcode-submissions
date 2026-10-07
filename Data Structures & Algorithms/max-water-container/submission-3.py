class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            width = j - i
            if (heights[i] > heights[j]):
                length = heights[j]
                area = width * length
                j -= 1
            else:
                length = heights[i]
                area = width * length
                i += 1
            maxArea = max(maxArea, area)
        
        return maxArea