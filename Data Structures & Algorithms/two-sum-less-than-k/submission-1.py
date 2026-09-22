class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        L = 0
        R = len(nums) - 1
        best = -1
        while L < R:
            sum = nums[L] + nums[R]
            if sum < k:
                L += 1
                best = max(best, sum)
            else:
                R -= 1

        return best

        