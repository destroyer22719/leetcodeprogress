from typing import List

class Solution:
  def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    newPaths = [[i+1] for i in range(n)]

    answers = [n] * len(queries)

    
    def dfs(i, dist_travelled, stop=n-1):
      if i == stop:
        return dist_travelled
      if i > stop:
        return n

      return min(dfs(j, dist_travelled + 1, stop) for j in newPaths[i])

    for q in range(len(queries)):
      query = queries[q]
      newPaths[query[0]].append(query[1])
      
      path2Q = dfs(0, 0, query[0])
      shortestPath = dfs(query[1], path2Q + 1)

      answers[q] = min(answers[q-1], shortestPath)

    
    return answers
    

sol = Solution()

a = sol.shortestDistanceAfterQueries(5, [[1,3],[2,4]])
print(a)


# a = sol.shortestDistanceAfterQueries(4, [[0,3],[0,2]])
# print(a)

# 787
# 848