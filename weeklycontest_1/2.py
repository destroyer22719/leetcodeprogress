from typing import List

class Solution:
  def countGoodNodes(self, edges: List[List[int]]) -> int:
    tree = {}

    for e in edges:
      if e[0] not in tree:
        tree[e[0]] = {
          "c": [e[1]],
          "s": 1
        }
      else:
        tree[e[0]]["c"].append(e[1])
        tree[e[0]]["s"] += 1

      if e[1] not in tree:    
        tree[e[1]] = {
          "c": [],
          "s": 1
        }

    def dfs_1(node, path):
      if tree[node]["c"] == []:
        for i in range(len(path) - 1, -1, -1):
          if i == len(path) - 1:
            tree[path[i]]["s"] += tree[node]["s"]
          else:
            tree[path[i]]["s"] += tree[path[i+1]]["s"]
      else:
        for c in tree[node]["c"]:
          dfs_1(c, list(path + [node]))
    
    dfs_1(0, [])

    result = 0
    def dfs_2(node):
      nonlocal result

      if len(tree[node]["c"]) <= 1:
        result += 1
      else:
        sizes = [tree[c]["s"] for c in tree[node]["c"]]
        counts = {i:sizes.count(i) for i in sizes}

        for size, count in counts.items():
          if count > 1:
            result += 1

      for c in tree[node]["c"]:
        dfs_2(c)
      
    dfs_2(0)

    return result

sol = Solution()
a = sol.countGoodNodes([[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]])

print(a)