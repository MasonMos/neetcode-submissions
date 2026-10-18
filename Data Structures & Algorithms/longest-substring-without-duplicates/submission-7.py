'''
Know:
- Given a string s
- Need to find the length of longest substring w/o dupes
- A substring is a contiguous sequene of chars

Approach:
- Use a sliding approach
- Using two pointer
- Need a variable to store the length of the longest window
- To prevent dupes, we can have a set
- If there are new chars (non-dupes), we can add them to the set
- If there are dupes, then we can remove them from the set
- The right pointer will increment the whole list
- The left pointer will increment behind the right pointer
 keeping track of the window, if there are dupes it will shrink the window
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        ans = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            ans = max(ans, r - l + 1)
        
        return ans










