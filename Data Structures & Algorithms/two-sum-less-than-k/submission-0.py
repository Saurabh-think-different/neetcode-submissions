class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        best = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if  sum < k:
                    best = max(best, sum)
        
        return best

        