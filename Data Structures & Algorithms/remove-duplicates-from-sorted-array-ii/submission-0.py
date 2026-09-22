class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        pos = 0
        cnt = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[pos]:
                nums[pos+1] = nums[i]
                pos += 1
                cnt = 0
            else:
                cnt += 1
                if cnt == 1:
                    nums[pos+1] = nums[i]
                    pos += 1
        return pos+1