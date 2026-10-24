import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        starters = []
        maxCount = 0

        for num in setNums:
            if num-1 not in setNums:
                starters.append(num)

        for num in starters:
            currCount = 1
            currNum = num
            while currNum + 1 in setNums:
                currCount += 1
                currNum += 1
            if currCount > maxCount:
                maxCount = currCount

        return maxCount