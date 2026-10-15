class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, l, s):
            if s == target:
                res.append(l.copy())
                return
            for j in range(i, len(nums)):
                if s + nums[j] > target:
                    return
                l.append(nums[j])
                dfs(j, l, s+nums[j])
                l.pop()
        
        dfs(0,[],0)
        return res
