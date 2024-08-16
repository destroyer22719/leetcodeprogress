class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    q = [[root, 0]]

    result = []
    curr_level = []
    curr_depth = 0
  
    if root is None:
      return result

    while q != []:
      n = q[0][0]
      depth = q[0][1]

      if curr_depth != depth:
        curr_depth = depth
        result.append(curr_level)
        curr_level = []
      curr_level.append(n.val)
    

      if n.left is not None:
        q.append([n.left, depth + 1])
      if n.right is not None:
        q.append([n.right, depth + 1])

      q.pop(0)
    result.append(curr_level)
    return result
      