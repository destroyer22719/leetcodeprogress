from typing import List

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    intervals = sorted(intervals, key=lambda x: x[0])
    intervalsB = sorted(intervals, key=lambda x: x[1])

    table = {str(i): False for i in intervals}

    # for i in range(1, len(intervals)):
    #   prev = intervals[i-1]
    #   curr = intervals[i]

    #   if prev[1] > curr[0]:
        