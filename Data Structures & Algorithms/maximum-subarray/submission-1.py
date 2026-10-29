class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        curr = 0

        for i in range(len(nums)):
            if nums[i] + curr > 0:
                curr += nums[i]
                total = max(total, curr)
            elif nums[i] > total:
                total = nums[i]
            else:
                curr = 0

        return total