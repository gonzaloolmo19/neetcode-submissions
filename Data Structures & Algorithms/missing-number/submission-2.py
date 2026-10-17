class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t = 0
        for i in range(len(nums)+1):
            t += i
        return t - sum(nums)
        