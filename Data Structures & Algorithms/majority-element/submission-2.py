class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # from collections import defaultdict
        # import math
        # n = len(nums)
        # maj = math.ceil(n/2)
        # ans = defaultdict(int)
        # for num in nums:
        #     ans[num] += 1
        #     if ans[num] >= maj:
        #         return num
        
        res = count = 0

        for n in nums:
            if count==0:
                res = n
            count += (1 if res == n else -1)
        return res

