class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = sum = nums[0]
        
        for e in nums[1:]:
            # Sum calculates best subarray currently
            sum = max(sum+e, e)

            # m stores the best subarray seen at the moment
            m = max(m, sum)

        return m