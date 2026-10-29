class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def jump(index):
            if index >= n-1: #final index reached
                return True

            reach = nums[index]

            if reach == 0: #base case cant jump
                return False

            for j in range(reach, 0, -1):
                work = jump(index+j)
                if work: return True
                nums[index+j] = 0

        if jump(0):
            return True
        return False
        
