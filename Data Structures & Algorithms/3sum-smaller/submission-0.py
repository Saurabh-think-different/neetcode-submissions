class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = []
        nums = sorted(nums)

        for i, a in enumerate(nums):
            L = i + 1
            R = len(nums) - 1

            while L < R:
                sum = a + nums[L] + nums[R]

                if sum < target:
                    for j in range(R, L, -1):
                        res.append([a, nums[L], nums[j]])
                    L += 1
                elif sum >= target:
                    R -= 1
            # print(res)
        return len(res)