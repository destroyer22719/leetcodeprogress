from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    toList = []

    curr = head

    while curr != None:
      toList.append(curr.val)
      curr = curr.next

    n = len(toList)
    maxPair = 0

    for i in range(0, n // 2):
      if toList[i] + toList[n-i-1] > maxPair:
        maxPair = toList[i] + toList[n-i-1]
    return maxPair
      