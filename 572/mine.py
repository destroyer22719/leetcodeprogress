# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
  def find_match(self, root, sub):
    if (root == None and sub == None) or ((sub != None and root != None and root.val == sub.val) and self.check_match(root, sub)):
      return True
    else:
      if root.left != None and self.find_match(root.left, sub):
        return True
      elif root.right != None and self.find_match(root.right, sub):
        return True
      return False

  def check_match(self, p, q):
    if p.val != q.val:
      return False
    if ((p.left == None or q.left == None )and q.left != p.left) or ((p.right == None or q.right == None )and q.right != p.right):
      return False
    if p.left != None and q.left != None and self.check_match(p.left, q.left) == False:
      return False
    if p.right != None and q.right != None and self.check_match(p.right, q.right) == False:
      return False
    return True

  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    return self.find_match(root, subRoot)