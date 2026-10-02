class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)

        i = 0
        j = n-1

        while i < j:
            capacity = (j-i) * min(heights[i], heights[j])

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
            res = max(res, capacity)
        
        return res