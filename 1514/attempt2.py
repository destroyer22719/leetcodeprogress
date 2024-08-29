
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

    def dijskstra(node, parent):