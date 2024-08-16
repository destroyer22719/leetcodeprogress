class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    p_path = []
    q_path = []

    def dfs(n, path):
      nonlocal p_path
      nonlocal q_path
      if n is None:
        return
      
      path = list(path)
      path.append(n)

      if n == p:
        p_path = path
      
      if n == q:
        q_path = path

      if q_path != [] and p_path != []:
        return
      
      dfs(n.left, path)
      dfs(n.right, path)

    dfs(root, [])

    answer = root
    for n in range(min(len(q_path), len(p_path))):
      if q_path[n] == p_path[n]:
        answer = q_path[n]
      else:
        break
    return answer