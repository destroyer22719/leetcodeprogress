from typing import List

class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals = sorted(intervals, key=lambda x: x[0])

    for i in range(1, len(intervals)):
      prev = intervals[i-1]
      curr = intervals[i]

      if prev[1] > curr[0]:
        return False
    return True
  
sol = Solution()
answer = sol.canAttendMeetings( [[7,10],[2,4]])

print(answer)