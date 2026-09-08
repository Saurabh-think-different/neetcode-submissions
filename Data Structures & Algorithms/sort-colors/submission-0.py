class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        for i in nums:
            buckets[i] += 1
        i = 0
        for c in range(len(buckets)):
            for j in range(buckets[c]):
                nums[i] = c
                i+=1


