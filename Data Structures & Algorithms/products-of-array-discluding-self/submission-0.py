class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                if zeros >= 2:
                    return [0 for _ in range(len(nums))]
            else:
                total *= num
        print(total)
        output = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            if num == 0:
                output[i] = total
            else:
                if zeros > 0:
                    output[i] = 0
                else:
                    output[i] = int(total / num)
        return output