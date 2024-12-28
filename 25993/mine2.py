from typing import List
import math

class Solution:
  def findScore(self, nums: List[int]) -> int:
    marked = min(nums)
    score = 0

    while marked != math.inf:
      marked = min(nums)
      markedInd = nums.index(marked)
      
      if markedInd != 0 and nums[markedInd - 1] != math.inf:
        nums[markedInd - 1] = math.inf
        markedInd -= 1
      if markedInd != len(nums) - 1 and nums[markedInd + 1] != math.inf:
        nums[markedInd + 1] = math.inf
      nums[markedInd] = math.inf
      score += marked
    return score
  
sol = Solution()
a = sol.findScore([2,1,3,4,5,2])
print(a)
