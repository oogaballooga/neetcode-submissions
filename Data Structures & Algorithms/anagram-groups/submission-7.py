class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp in anagrams:
                anagrams[temp].append(s)
            else: 
                anagrams[temp] = [s]
        return list(anagrams.values())