class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(start, path, total):
            if total == target:
                results.append(path.copy())
                return

            for i in range(start, len(nums)):
                num = nums[i]
                if num + total <= target:
                    path.append(num)
                    backtrack(i, path, total+num)
                    path.pop()
        backtrack(0, [], 0)
        return results