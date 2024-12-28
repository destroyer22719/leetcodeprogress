from typing import List


class Solution:
  def findScore(self, nums: List[int]) -> int:
    score = 0
    remaining = list(nums)

    while remaining != []:
      marked = min(remaining)
      markedIndex = remaining.index(marked)

      if markedIndex != 0 and remaining[markedIndex-1] == nums[nums.index(marked)-1]:
        del remaining[markedIndex-1]
        markedIndex -= 1
      if markedIndex != len(remaining) - 1 and remaining[markedIndex+1] == nums[nums.index(marked)+1]:
        del remaining[markedIndex+1]
      del remaining[markedIndex]
      score += marked 
    return score
  
sol = Solution()
a = sol.findScore([10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42])
print(a)
