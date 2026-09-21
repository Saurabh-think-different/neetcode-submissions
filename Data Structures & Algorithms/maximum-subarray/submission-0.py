class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import math
        best = curr_sum = -math.inf
        for num in nums:
            curr_sum = max(num, num+curr_sum)
            best = max(best, curr_sum)
        return best