class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        nums_cnt = defaultdict(int)
        res = []
        for e in nums:
            nums_cnt[e] += 1
        
        for i in range(n-2):
            nums_cnt[nums[i]]-=1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                nums_cnt[nums[j]]-=1
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                target = -nums[i] -nums[j]
                if nums_cnt[target] > 0:
                    res.append([nums[i], nums[j], target])
            for j in range(i+1, n):
                nums_cnt[nums[j]] += 1
        return res

        