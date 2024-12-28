from typing import List

class Solution:
  def maxScoreSightseeingPair(self, values: List[int]) -> int:
    answer = 0
    max_b = values[-1] - (len(values) - 1)

    for i in range(len(values) - 2, -1, -1):
      answer = max(answer, values[i] + i + max_b)
      max_b = max(max_b, values[i] - i)
    return answer

