class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exist = set(nums)

        for i in range(len(nums)+1):
            if not i in exist:
                return i
        