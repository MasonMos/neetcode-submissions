class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            newWord = "".join(sorted(word))
            if newWord not in seen:
                seen[newWord] = [word]
            else:
                seen[newWord].append(word)

        return list(seen.values())