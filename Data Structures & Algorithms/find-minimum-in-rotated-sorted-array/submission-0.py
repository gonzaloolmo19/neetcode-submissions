class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        res = nums[0]

        while l <= r:
            # sublist sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # sublist not sorted
            mid = (l + r) // 2
            res = min(res, nums[mid])
            # left sublist sorted, we only search the right sublist
            if nums[l] <= nums[mid]:
                l = mid+1
            # right sublist sorted, we only search the left sublist
            else:
                r = mid-1
        
        return res
            
