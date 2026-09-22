class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = 0
        R = len(nums) - 1

        while L < R:
            sum = nums[L] + nums[R]
            if sum > target:
                R -= 1
            elif sum < target:
                L += 1
            elif sum == target:
                return [L+1, R+1]
        return []