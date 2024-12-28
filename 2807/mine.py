# Definition for singly-linked list.
from typing import Optional
import math

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head

    while curr != None:
      if curr.next == None:
        break

      between = ListNode(math.gcd(curr.val, curr.next.val))
      between.next = curr.next
      curr.next = between

    return head
    