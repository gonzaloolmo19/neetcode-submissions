class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        cache = [(0,0)] * len(nums)
        cache[0] = (0, nums[0])
        cache[1] = (nums[0], nums[1])

        for i in range(2, len(nums)):
            cache[i] = (max(cache[i-1][0], cache[i-1][1]), cache[i-1][0]+nums[i])
        
        return max(cache[-1][0], cache[-1][1])

