from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = None
    tail = head

    while list1 and list2:
      if list1.val == list2.val:
        n1 = ListNode()
        n1.val = list1.val
        
        n2 = ListNode()
        n2.val = list2.val
        n1.next = n2

        if head == None:
          head = n1
          tail = head.next
        else:
           tail.next = n1
           tail = tail.next.next
        list1 = list1.next
        list2 = list2.next
      elif list1.val > list2.val:
        n = ListNode()
        n.val = list2.val

        list2 = list2.next

        if head == None:
          head = n
          tail = head
        else:
          tail.next = n
          tail = tail.next
      else:
        n = ListNode()
        n.val = list1.val 

        list1 = list1.next

        if head == None:
          head = n
          tail = head
        else:
          tail.next = n
          tail = tail.next
    if list1 == None and list2 != None:
      if head == None:
        head = list2
      else:
        tail.next = list2
    elif list2 == None and list1 != None:
      if head == None:
        head = list1
      else:
        tail.next = list1
    return head
        
# Linked List 1: 3 -> 7 -> 1
node1_3 = ListNode(9)
node1_2 = ListNode(7, node1_3)
node1_1 = ListNode(3, node1_2)

# Linked List 2: 5 -> 2 -> 9
node2_3 = ListNode(10)
node2_2 = ListNode(6, node2_3)
node2_1 = ListNode(3)

sol = Solution()
a = sol.mergeTwoLists(None, node2_1)
print(a)

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
print_linked_list(a)

