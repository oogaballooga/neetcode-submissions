class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = l + r // 2
        minimum = min(nums[l], nums[mid], nums[r])
        while l < r:
            if nums[r] < nums[mid]: #rotation point to the right
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2
            minimum = min(minimum, nums[l], nums[mid], nums[r])
        return minimum