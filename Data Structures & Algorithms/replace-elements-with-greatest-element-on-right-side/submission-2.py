class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        maxi = -1
        for i in range(len(arr)-1, -1, -1):
            res.append(maxi)
            maxi = max(arr[i], maxi)

        return res[::-1]