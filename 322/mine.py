from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                for c in coins:
                    if c > i:
                        continue
                    if dp[i - c] == -1:
                        continue
                    if dp[i] == -1:
                        dp[i] = 1 + dp[i - c]
                    else:
                        dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount]
    
sol = Solution()

answer = sol.coinChange([2], 3)
print(answer)