class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sHash = ''.join(sorted(s))
            if sHash in anagrams:
                anagrams[sHash].append(s)
            else:
                anagrams[sHash] = [s]
        return list(anagrams.values())