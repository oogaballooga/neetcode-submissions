class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        
        while l <= r:
            if nums[mid] == target: # mid is target
                return mid
            if nums[l] <= nums[mid]: # left sorted
                if target >= nums[l] and target <= nums[mid]: # and target is within left
                    r = mid - 1
                else: l = mid + 1
            elif target >= nums[mid] and target <= nums[r]: #right sorted and target within right
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2
        return -1