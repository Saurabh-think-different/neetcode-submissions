class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        import math
        n = len(nums)
        maj = math.ceil(n/2)
        ans = defaultdict(int)
        for num in nums:
            ans[num] += 1
            if ans[num] >= maj:
                return num
        

