from typing import List


class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    adj = { node: [] for node in range(n) }

    for e in edges:
      adj[e[0]].append(e[1])
      adj[e[1]].append(e[0])

    visited = {}

    def dfs(n, parent=n):
      visited[n] = True

      for neighbour in adj[n]:
        if neighbour == parent:
          continue
        if neighbour in visited or not dfs(neighbour, n):
          return False
      return True
    
    return dfs(0) and len(visited.keys()) == n

sol = Solution()
answer = sol.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])
print(answer)
