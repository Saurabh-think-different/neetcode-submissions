class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        count = 0

        nums = sorted(set(nums))
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        print(nums)
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                count +=1
            else:
                count = 0
            
            best = max(best, count+1)
        return best