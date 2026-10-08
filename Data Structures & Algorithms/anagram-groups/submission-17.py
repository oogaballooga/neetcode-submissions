class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}
        for s in strs:
            code = ''.join(sorted(s))
            if code in anaDict:
                anaDict[code].append(s)
            else:
                anaDict[code] = [s]
        return list(anaDict.values())