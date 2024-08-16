# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
  def dfs(self, p, q):
    if p.val != q.val or (q.left != None and p.right != None and q.left.val != p.left.val):
      return False
    
    if p.left != None and q.left != None and self.dfs(p.left, q.left) == False:
      return False
    if p.right != None and q.right != None and self.dfs(p.right, q.right) == False:
      return False
    
    return True

  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    return self.dfs(p, q)