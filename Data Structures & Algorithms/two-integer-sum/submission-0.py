class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        ans = []
        for i, num in enumerate(nums):
            if num in s:
                print(s.get(num))
                print("hi")
                ans = [s[num], i]
                return ans
            else:
                diff = target - num
                s[diff] = i
        print(s)
        return ans
