class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = -110000
        m = -110000
        for e in nums:
            sum = max(sum+e, e)
            m = max(m, sum)

        return m