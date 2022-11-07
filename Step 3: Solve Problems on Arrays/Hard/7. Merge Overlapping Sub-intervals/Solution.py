class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def takeFirst(elem):
            return (elem[0])
        intervals.sort(key= takeFirst)
        i=1
        while i<len(intervals):
            if intervals[i-1][1]>=intervals[i][0]:
                if intervals[i-1][1]<=intervals[i][1]:
                    intervals[i-1][1]= intervals[i][1]
                    intervals.remove(intervals[i])
                else:
                    intervals.remove(intervals[i])
            else:
                i+=1
        return intervals
