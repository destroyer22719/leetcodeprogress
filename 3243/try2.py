from typing import List


class Solution:
  def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    newPaths = [[i+1] for i in range(n)]
    answers = []
    dp = {n-1: 0}

    for q in range(len(queries)):
      if 0 in dp and dp[0] == 1:
        answers.append(1)
        continue

      query = queries[q]
      newPaths[query[0]].append(query[1])

      if len(dp) != n:
        for i in range(n-2, -1, -1):
          if len(newPaths[i]) == 1:
            dp[i] = 1 + dp[i+1]
          else:
            dp[i] = 1 + min(dp[j] for j in newPaths[i])
      else:
        for i in range(query[0], -1, -1):
          if len(newPaths[i]) == 1:
            dp[i] = 1 + dp[i+1]
          else:
            dp[i] = 1 + min(dp[j] for j in newPaths[i])
      answers.append(dp[0])
      
    return answers
  
sol = Solution()

a = sol.shortestDistanceAfterQueries(5,[[2,4],[0,2],[0,4]])
print(a)

a = sol.shortestDistanceAfterQueries(4, [[0,3],[0,2]])
print(a)

a = sol.shortestDistanceAfterQueries(4, [[0,3],[0,2]])
print(a)