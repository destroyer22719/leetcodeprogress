from typing import List

class Solution:
  def maxScoreSightseeingPair(self, values: List[int]) -> int:
    left = 0
    right = len(values) - 1

    answer = 0

    while left < right:
      score = values[left] + values[right] + left - right, answer
      answer = max(score, answer)
      if values[left] < values[right]:
        left += 1
      elif values[left] == values[right]:
        if values[left + 1] >= values[right - 1]:
          left += 1
        else:
          right -=1
      else:
        right -= 1
    return answer
  
sol = Solution()
a = sol.maxScoreSightseeingPair([3,7,2,3])
print(a)