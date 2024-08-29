from typing import List

class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    tree = {}
    result = {}

    for i in range(n):
      tree[i] = {
        "neighbour": [],
        "weight": []
      }

      result[i] = 0
    result[start_node] = 1

    i = 0
    for e in edges:
      tree[e[0]]["neighbour"].append(e[1])
      tree[e[0]]["weight"].append(succProb[i])

      tree[e[1]]["neighbour"].append(e[0])
      tree[e[1]]["weight"].append(succProb[i])

      i += 1

    visited = {}
    unvisited = dict(result)

    def dijskstra(node):
      nonlocal unvisited
      visited[node] = True


      for i in range(len(tree[node]["neighbour"])):
        neighbour = tree[node]["neighbour"][i]

        if neighbour not in visited:
          result[neighbour] = max(result[neighbour], result[node]*tree[node]["weight"][i])
          unvisited[neighbour] = result[neighbour]

      del unvisited[node]

      if len(unvisited) != 0:
        dijskstra(max(unvisited, key=unvisited.get))



    dijskstra(start_node)

    return result[end_node]

sol = Solution()
a = sol.maxProbability(3,  [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)
print(a)