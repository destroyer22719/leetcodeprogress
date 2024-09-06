# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

class Solution:
  def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

    nums = {i for i in nums}

    new_head = ListNode(head.val) if head.val not in nums else None
    curr = head

    while curr != None:
      if curr.val not in nums:
        if new_head == None:
          new_head = ListNode(curr.val)
        else:
          new_head.next = curr.val
      curr = curr.next
    return new_head
