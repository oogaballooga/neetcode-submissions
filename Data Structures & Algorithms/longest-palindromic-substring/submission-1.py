class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPal = s[0]

        for i in range(len(s)*2-1):
            mid = i / 2
            for offset in range(1, len(s)):
                trueNegOffset = math.ceil(mid-offset)
                truePosOffset = math.floor(mid+offset)
                if trueNegOffset < 0 or truePosOffset >= len(s):
                    break
                if s[trueNegOffset] == s[truePosOffset]:
                    if offset*2 + 1 > len(longestPal):
                        longestPal = s[trueNegOffset:truePosOffset+1]
                else:
                    break
        return longestPal