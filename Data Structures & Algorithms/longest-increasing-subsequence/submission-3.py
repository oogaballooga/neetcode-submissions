class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = 1
        
        dp = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    longest = max(longest, dp[i])
        return longest