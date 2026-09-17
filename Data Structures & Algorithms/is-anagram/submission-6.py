class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        for letter in s:
            if letter not in hm1:
                hm1[letter] = 1
            else:
                hm1[letter] += 1
        
        for letter in t:
            if letter not in hm2:
                hm2[letter] = 1
            else:
                hm2[letter] += 1
        
        return hm1 == hm2