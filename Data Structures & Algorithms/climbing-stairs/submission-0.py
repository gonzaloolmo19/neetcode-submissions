class Solution:
    def climbStairs(self, n: int) -> int:
        m = [0] * n
        m[0] = 1

        if n >= 2:
            m[1] = 2

        for i in range(2, n):
            m[i] = m[i-1] + m[i-2]
        
        return m[n-1]
            
