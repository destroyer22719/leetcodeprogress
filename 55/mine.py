from typing import List

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    currVal = nums[0]
    currInd = 0

    n = len(nums)

    if n == 1:
      return True

    while True:
      if currInd + currVal >= n - 1:
        return True

      start = currInd + 1
      interval = nums[start: currVal + start]

      intLen = len(interval)

      if intLen == 0:
        return False
      
      maxVal = interval[0] 
      maxInd = 0


      for i in range(intLen):
        if i + interval[i] > maxVal:
          maxVal = interval[i] + i
          maxInd = i
      
      # if i + interval[i] >= n - 1:
      #   return True
    
      currInd += maxInd + 1
      currVal = nums[currInd]
      
sol = Solution()

answer = sol.canJump([3,2,1,0,4])
print(answer)
