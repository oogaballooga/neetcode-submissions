class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        previ = None
        for i, num in enumerate(nums[:-2]):
            if num == previ:
                continue
            previ = num
            prevl = None
            l = i+1
            r = len(nums) - 1
            target = -num
            while l < r:
                if nums[l] + nums[r] == target and nums[l] != prevl:
                    output.append([nums[i], nums[l], nums[r]])
                    prevl = nums[l]
                    while l < r and nums[l] == prevl:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
        return output