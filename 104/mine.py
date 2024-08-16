# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
  def dfs(self, node, depth):
    self.max = max(self.max, depth)

    if node.left != None:
      self.dfs(node.left, depth + 1)
    if node.right != None:
      self.dfs(node.right, depth + 1)

  def maxDepth(self, root: Optional[TreeNode]) -> int:
    self.max = 1

    if (root == None or root.val == None):
      return 0

    self.dfs(root, 1)
    return self.max
