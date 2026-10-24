class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxP = 0
        for val in prices:
            buy = min(buy, val)
            maxP = max(maxP, val-buy)
        return maxP