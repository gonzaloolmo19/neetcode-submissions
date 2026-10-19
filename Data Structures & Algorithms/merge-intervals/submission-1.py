class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        i = 0
        n = len(intervals)
        while i < n :
            end = i
            if i == n-1 or intervals[i][1] < intervals[i+1][0]:
                res.append(intervals[i])
            else:
                end = i + 1
                newInterval = intervals[i]
                while end < n and intervals[i][1] >= intervals[end][0]:
                    newInterval[1] = max(newInterval[1], intervals[end][1])
                    end += 1
                res.append(intervals[i])
            i = max(i+1, end)
        return res
                    
                
