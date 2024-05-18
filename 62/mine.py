class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for j in range(m):
      for i in range(n):
        if i >= 1:
          dp[j][i] += dp[j][i-1]
        if j >= 1:
          dp[j][i] += dp[j-1][i]
    
    return dp[m-1][n-1]
  
sol = Solution()
answer = sol.uniquePaths(3, 7)
print(answer)