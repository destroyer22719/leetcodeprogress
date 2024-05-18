class Solution:
  def numDecodings(self, s: str) -> int:
    # n = len(s)
    # dp = [0]*n

    # if s[0] == "0":
    #   return 0

    # dp[0] = 1

    # for i in range(1, n):
    #   prevNum = int(s[i-1])
    #   curNum = int(s[i])

    #   if (curNum == 0 and prevNum > 2) or (curNum == 0 and prevNum == 0):
    #     return 0
    #   elif prevNum == 0 or prevNum >= 3 or (prevNum == 2 and curNum > 6):
    #     dp[i] = dp[i-1]
    #   elif curNum == 0 and prevNum <= 2:
    #     dp[i] = max(dp[i-1] - 1, 1)
    #   else:
    #     dp[i] = max((dp[i-1]-1)*2 + 1, dp[i-1]+1)

    # return dp[-1]
    if not s or s[0] == '0':
      return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, n + 1):
        one_digit = int(s[i-1:i])
        two_digits = int(s[i-2:i])

        if 1 <= one_digit <= 9:
            dp[i] += dp[i-1]
        if 10 <= two_digits <= 26:
            dp[i] += dp[i-2]

    return dp[n]

sol = Solution()
answer = sol.numDecodings("123")
print(answer)