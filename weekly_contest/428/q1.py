from typing import List

class Solution:
  def buttonWithLongestTime(self, events: List[List[int]]) -> int:
    dist = events[0][1]
    answer = events[0][0]
    for i in range(1, len(events)):
      if events[i][1] - events[i-1][1] > dist:
        answer = events[i][0]
        dist = events[i][1] - events[i-1][1]
      elif dist == events[i][1] - events[i-1][1] and answer > events[i][0]:
        answer = events[i][0]
    return answer