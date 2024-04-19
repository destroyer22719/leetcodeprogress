from typing import List


class Solution:
  def findLongestChain(self, pairs: List[List[int]]) -> int:
    pairs = sorted(pairs, key=lambda x: x[0])

    dp = [1]*len(pairs)

    for i in range(1, len(pairs)):
      for j in range(i):
        if pairs[j][1] < pairs[i][0]:
          dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
  
sol = Solution()

answer = sol.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]])
print(answer)
