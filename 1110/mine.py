class Solution:
  def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    result = [root]

    def dfs(n, direction="", parent=None, in_res=True):
      if n is None:
        return
      
      if n.val not in to_delete and in_res==False:
        result.append(n)

      if n.val in to_delete:
        if parent and direction:
          if direction == "left":
            parent.left = None
          elif direction == "right":
            parent.right = None
        to_delete.remove(n.val)

        dfs(n.left, "left", n, False)
        dfs(n.right, "right", n, False)
      else:
          dfs(n.left, "left", n, True)
          dfs(n.right, "right", n, True)

    dfs(root)

    return result

