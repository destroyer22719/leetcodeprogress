from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    newInterval = [intervals[0]]
    for i in list(range(1, len(intervals))):
      a = newInterval[-1]
      b = intervals[i]

      if a[1] >= b[0]:
        merged = [min(a[0], b[0]), max(a[1], b[1])]
        newInterval.pop()
        newInterval += [merged]
      else:
        newInterval += [intervals[i]]

    return newInterval
  
sol = Solution()  

a = sol.merge([[1,4],[0,0]])
print(a)
