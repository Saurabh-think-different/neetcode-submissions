class Solution:
    arr = [-1] * 46
    def climbStairs(self, n: int) -> int:
        if Solution.arr[n] != -1:
            return Solution.arr[n]
        if n == 1:
            Solution.arr[1] = 1
            return Solution.arr[1]
        elif n == 2:
            Solution.arr[2] = 2
            return Solution.arr[2]
        
        Solution.arr[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return Solution.arr[n]
        