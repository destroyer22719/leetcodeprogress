# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
  def dfs(self, n: Optional[TreeNode]):
    if n == None:
      return None
    
    temp = n.left

    n.left = n.right
    n.right = temp

    self.dfs(n.left)
    self.dfs(n.right)

    return n

  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    return self.dfs(root)