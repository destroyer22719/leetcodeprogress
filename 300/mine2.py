from typing import List

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1]*n


    maxLIS = 1

    for i in range(n - 1, -1, -1):
      local_maxLIS = 1
      for j in range(i, n):
        if nums[i] < nums[j] and local_maxLIS < 1 + dp[j]:
          local_maxLIS = dp[i] = 1 + dp[j]
      maxLIS = max(local_maxLIS, maxLIS)  
    return maxLIS
  
sol = Solution()
answer = sol.lengthOfLIS([10,9,2,5,3,7,101,18])
print(answer)
