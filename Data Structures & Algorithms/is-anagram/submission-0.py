from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Scount = Counter(s)
        Tcount = Counter(t)
        return Scount == Tcount