class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        final_res = 0
        nums = sorted(nums)

        for i, a in enumerate(nums):
            res = 0
            L = i + 1
            R = len(nums) - 1

            while L < R:
                sum = a + nums[L] + nums[R]
                if sum < target:
                    res += R-L
                    L += 1
                elif sum >= target:
                    R -= 1
            final_res += res
        return final_res