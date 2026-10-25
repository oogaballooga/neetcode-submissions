class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sub = set()
        l, r, longest = 0, 0, 1
        sub.add(s[0])
        while r < len(s) - 1:
            r += 1
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
