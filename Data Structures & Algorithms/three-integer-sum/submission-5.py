class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-2):
            a = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if a > 0:
                continue

            l = i+1
            r = n-1
            while l < r:
                s = a + nums[l] + nums[r]
                if s > 0:
                    r -=1
                elif s < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
            


        

        