class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        buckets = [[] for _ in range(len(nums))]
        for num, value in freq.items():
            buckets[value-1].append(num)
        
        output = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output