from typing import List


class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [{"v": 1, "s": None}]*(len(nums))
    dp[len(nums) - 1] = {"v":1, "s": nums[-1]}
    
    for i in range(len(nums) - 2, -1, -1):
      max_dp = 0
      for j in range(i + 1, len(nums)):
        if nums[i] < dp[j]["s"] and dp[j]["v"] > max_dp:
          max_dp = dp[j]["v"]
      if max_dp + 1 > dp[i + 1]["v"]:
        dp[i] = { "v": max_dp + 1, "s": nums[i]}
      else:
        dp[i] = dp[i + 1]
    return dp[0]["v"]
  
sol = Solution()

answer = sol.lengthOfLIS([0,1,0,3,2,3])
print(answer)
