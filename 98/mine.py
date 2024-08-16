class Solution:
  def dfs(self, n, min_v, max_v):
    if (min_v == None or n.val > min_v ) and (max_v == None or n.val < max_v) and (n.left == None or n.left.val < n.val) and (n.right == None or n.right.val >= n.val):
      if n.left != None and not self.dfs(n.left, min_v, n.val):
        return False
      elif n.right != None and not self.dfs(n.right, n.val, max_v):
        return False
      return True
    else:
      return False
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    return self.dfs(root, None, None)