class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        
        ans = 0
        nums = sorted(nums)
        
        L = 0
        R = len(nums) - 1

        while L <= R:
            if nums[L] + nums[R] <= limit:
                ans += 1
                L += 1
                R -= 1
            elif nums[R] >= nums[L] and nums[R] <= limit:
                ans += 1
                R -= 1
        
        return ans


