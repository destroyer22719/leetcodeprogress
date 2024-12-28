class Node():
  val = None
  children = {}

  def __init__(self, val, children=None) -> None:
    self.val = val
    if children:
      self.children = children
    else:
      self.children = {}
class Solution:
  def findKthNumber(self, n: int, k: int) -> int:
    root = Node(0)
    curr_node = root
    curr_str = ""

    def get_curr(val):
      curr = root

      for i in val:
        curr = curr.children[int(i)]
      return curr

    for i in range(1, n+1):
      if str(i)[:-1] != curr_str:
        curr_node = get_curr(str(i)[:-1])
        curr_str = str(i)[:-1]

      curr_node.children[int(str(i)[-1])] = Node(int(str(i)[-1]), {})

    result = []

    def dfs(n, path):
      nonlocal result
      if len(result) == k:
        return result[-1]
      if path != "":
        result.append(int(path))

      for i in n.children.items():
        if len(result) != k:
          dfs(n.children[i[0]], str(path) + str(i[0]))
        else:
          break
    dfs(root, "")
    return result[-1]
      
sol = Solution()
a = sol.findKthNumber(13, 2)
print(a)