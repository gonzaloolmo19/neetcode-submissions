class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        last = (nums[0], nums[1])
        current = (0,0)
        for i in range(2, len(nums)):
            current = (max(last[0], last[1]), last[0]+nums[i])
            last = current
        
        return max(current[0], current[1])

