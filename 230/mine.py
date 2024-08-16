class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    def dfs(n):
      if n is None:
        return []
      
      return dfs(n.left) + [n.val] + dfs(n.right)
    
    return dfs(root)[k-1]