from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    # if (len(nums) == 1):
    #   return nums[0]
    # elif (len(nums) == 2):
    #   return max(nums[0], nums[1])
    
    # dp = [0]*(len(nums))
    # dp[0] = nums[0]
    # dp[1] = max(nums[0], nums[i])

    # for i in range(2, len(nums)):     
    #   dp[i] = dp[i - 1]   
    #   for j in range(2, i + 1):
    #     dp[i] = max(nums[i] + dp[i - j], dp[i])

    # return dp[-1]
    if (len(nums) == 1):
      return nums[0]

    
    dp = [0]*(len(nums))
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
      dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[-1]
  
sol = Solution()

answer = sol.rob([2,1,1,2])
print(answer)

answer = sol.rob([2,7,9,3,1])
print(answer)

answer = sol.rob([1,10,1,1,10,1])
print(answer)

answer = sol.rob([2,1])
print(answer)