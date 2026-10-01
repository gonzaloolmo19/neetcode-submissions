class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_zeros = 0
        zero_index = -1
        prod = 1
        res = [0] * len(nums)
        for i, e in enumerate(nums):
            if e == 0:
                n_zeros +=1
                zero_index = i
            else:
                prod *= e

        print(n_zeros)
        if n_zeros >= 2:
            return res
        elif n_zeros == 1:
            res[zero_index] = prod
        else:
            for i in range(len(nums)):
                res[i] = int(prod/nums[i])

        
        return res
            

