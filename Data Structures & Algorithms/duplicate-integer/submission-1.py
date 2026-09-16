class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict

        c = defaultdict(int)

        for num in nums:
            c[num] += 1
            if c[num] > 1:
                return True
        
        return False