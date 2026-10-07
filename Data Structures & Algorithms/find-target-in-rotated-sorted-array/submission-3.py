class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First we search the split point

        l, r = 0, len(nums)-1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid +1
        
        print(l, nums[l])
        split = l
        l, r = 0, split -1

        while l <= r:
            mid = (l + r) // 2
            print(nums[mid], target)
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

       
        
        l, r = split, len(nums) -1

        while l <= r:
            mid = (l + r) // 2
            print(nums[mid], target)

            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

        