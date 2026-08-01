class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        removed = 0
        end = intervals[0][1]

        for start, finish in intervals[1:]:
            if start >= end:
                end = finish
            else:
                removed += 1

        return removed