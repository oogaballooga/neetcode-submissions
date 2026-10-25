class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = l + r // 2
        while l < r:
            if nums[r] < nums[mid]: #rotation point to the right
                l = mid + 1
            else:
                r = mid
            mid = (l + r) // 2
        return nums[l]