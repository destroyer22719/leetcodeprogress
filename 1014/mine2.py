from typing import List

class Solution:
  def maxScoreSightseeingPair(self, values: List[int]) -> int:
    left = 0
    right = len(values) -1

    answer = 0

    while left < right:
      answer = max(answer, values[left] + left + values[right] - right)
      if values[left] + left <= values[right] - right:
        left += 1
      else:
        right -= 1
      
      if left == right:
        break
    return answer

  
sol = Solution()
a = sol.maxScoreSightseeingPair([1,2,2])
print(a)