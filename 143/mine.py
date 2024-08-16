class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    curr = head.next
    prev = head

    nodes = []

    while curr != None:
      nodes.append(curr)
      curr = curr.next

    isFirst = False
    tail = head

    while len(nodes) > 0:
      if isFirst:
        tail.next = nodes.pop(0)
      else:
        tail.next = nodes.pop()
      isFirst = not isFirst
      tail = tail.next

      if tail.next.next is not None:
        tail.next.next = None
    return head