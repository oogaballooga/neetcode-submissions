class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}
        for s in strs:
            code = str(sorted(s))
            if code in anaDict:
                anaDict[code].append(s)
            else:
                anaDict[code] = [s]
        return [anaDict[x] for x in anaDict.keys()]