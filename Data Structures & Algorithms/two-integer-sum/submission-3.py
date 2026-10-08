class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}
        for i, num in enumerate(nums):
            if target-num in dictNums:
                return [dictNums[target-num], i]
            dictNums[num] = i