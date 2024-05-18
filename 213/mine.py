from typing import List


class Solution:
  def rob(self, nums: List[int]) -> int:
    if (len(nums) == 1):
      return nums[0]
    
    dp = [0]*(len(nums))
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    containsFirst = [0]
    if dp[1] == dp[0] and nums[0] != nums[1]:
      containsFirst.append(1)

    for i in range(2, len(nums)):
      if i != len(nums) - 1:
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        if (dp[i] == nums[i] + dp[i - 2] and i - 2 in containsFirst) or (dp[i] == dp[i - 1] and i - 1 in containsFirst):
          containsFirst.append(i)
      else:
        if i - 2 in containsFirst:
          dp[i] = max(dp[i - 2], nums[i] + dp[i - 2] - dp[0], dp[i - 1])
        else:
          dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[-1]
  
sol = Solution()
answer = sol.rob([2,2,4,3,2,5])
print(answer)