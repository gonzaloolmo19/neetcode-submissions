class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        one = (nums[0], nums[1])
        current = (0,0)
        for i in range(2, len(nums)):
            current = (max(one[0], one[1]), one[0]+nums[i])
            one = current
        
        return max(current[0], current[1])

