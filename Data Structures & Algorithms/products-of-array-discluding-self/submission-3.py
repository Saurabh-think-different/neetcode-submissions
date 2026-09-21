class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        cnt_zero = 0
        idx_zero = []
        product = 1

        ans = [0] * len(nums)

        for i, num in enumerate(nums):
            if num == 0:
                cnt_zero += 1
                idx_zero.append(i)
            else:
                product *= num

        if cnt_zero > 1:
            return ans
        elif cnt_zero == 1:
            ans[idx_zero[0]] = product
        else:
            for i in range(len(nums)):
                ans[i] = product // nums[i]
        
        return ans
