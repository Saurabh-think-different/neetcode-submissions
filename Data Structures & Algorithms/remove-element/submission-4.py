class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1

        while (i<=j):
            print(nums, i, j)
            if nums[i] != val:
                i+=1
            else:
                if nums[j] != val:
                    nums[j], nums[i] = nums[i], nums[j]
                    i+=1
                    j-=1
                else:
                    j-=1
        return i
