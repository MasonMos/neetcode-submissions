class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        ans = 0

        l = 0

        for r in range(len(s)): 
            chars[s[r]] = 1 + chars.get(s[r], 0)

            while (r-l + 1) - max(chars.values()) > k:
                chars[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans