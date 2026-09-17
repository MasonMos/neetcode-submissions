class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for string in strs:
            sortedStrLst = sorted(string)
            sortedStr = "".join(sortedStrLst)
            if sortedStr not in words:
                words[sortedStr] = [string]
            elif sortedStr in words:
                words[sortedStr].append(string)
        
        return list(words.values())