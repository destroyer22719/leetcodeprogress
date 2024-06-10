from typing import List


class Solution:
  def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    dp = list(profit)

    maxProfit = 0

    for i in range(len(dp) - 1, -1, -1):
      for j in range(len(dp)):
        if i != j:
          if endTime[i] <= startTime[j]:
            dp[i] = max(dp[i], profit[i] + dp[j])
          elif endTime[j] <= startTime[i]:
            dp[j] = max(dp[j], profit[j] + dp[i])
        maxProfit = max(maxProfit, dp[i], dp[j])

    return maxProfit

sol = Solution()
a = sol.jobScheduling([6,15,7,11,1,3,16,2], [19,18,19,16,10,8,19,8], [2,9,1,19,5,7,3,19])
print(a)