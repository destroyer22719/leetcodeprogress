from typing import List


class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    if edges == []:
      return 0

    adj = { node: [] for node in range(n) }

    for e in edges:
      adj[e[0]].append(e[1])
      adj[e[1]].append(e[0])

    visited = {}

    def dfs(node):
      if node in visited:
        return
      
      visited[node] = True

      for neighbour in adj[node]:
        if neighbour in visited:
          continue
        dfs(neighbour)

    i = 0
    for node in range(n):
      if node not in visited:
        i += 1
        dfs(node)
    return i
  
sol = Solution()
answer = sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]])
print(answer)
