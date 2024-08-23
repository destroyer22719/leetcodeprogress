import math

class Solution:
  def minSteps(self, n: int) -> int:
    dp = {
      1: 0,
      2: 2
    }

    def amt(val):
      result = val
      for i in range(2, val // 2):
        if val % i == 0:
          result = min(result, dp[i]+int(val/i))
      dp[val] = result

    if n == 1:
      return 0
    dp[n] = n
    for i in range(2, n // 2):
      amt(i)

      if n % i == 0:
        dp[n] = min(dp[n], dp[i]+int(n/i))
    return dp[n]
  
sol = Solution()
a = sol.minSteps(18)
print(a)
