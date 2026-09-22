class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1

        best = 0

        while L < R:
            area = (R-L) * min(heights[L], heights[R])
            best = max(area, best)
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1

        return best