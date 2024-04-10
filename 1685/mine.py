from typing import List

class Solution:
  def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0]*n

    leftSum = 0
    rightSum = sum(nums)

    leftAmt = 0
    rightAmt = n

    for i in range(n):
      rightAmt -= 1
      rightSum -= nums[i]

      result[i] = (leftAmt*nums[i] - leftSum) + (rightSum - rightAmt*nums[i])

      leftAmt += 1
      leftSum += nums[i]
    
    return result
  
sol = Solution()
answer = sol.getSumAbsoluteDifferences([1, 2])

print(answer)
