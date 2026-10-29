class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1: return nums[0]

        def search(houses):
            dp = [0] * n
            dp[0] = 0
            dp[1] = houses[0]
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i-1])
            return dp[n-1]
        
        return max(search(nums[1:]), search(nums[:-1]))