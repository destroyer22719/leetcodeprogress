from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next

class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    head = None
    tail = None

    def findMins():
      nonlocal lists

      mins = []
      fixed_list = []
      curr_i = 0
      for i in range(len(lists)):
        if lists[i] != None:
          if mins == [] or lists[i].val <= mins[0][0].val:
            mins = [[lists[i], curr_i]]
          elif lists[i].val == mins[0][0].val:
            mins += [lists[i],curr_i]
          fixed_list.append(lists[i])
          curr_i += 1

      lists = fixed_list

      return mins
    
    def removeVals(myLists):
      for l, i in myLists:
        if l != None:
          lists[i] = lists[i].next
          if lists[i] == None:
            lists.pop(i)
        else:
          lists.pop(i)
          
    def addToLL(vals):
      nonlocal head
      nonlocal tail 

      if vals == []:
        return

      new_head = ListNode()
      new_head.val = vals[0][0].val

      new_tail = new_head
      for x in range(1, len(vals)):
        n = ListNode()
        n = vals[x][0].val
        new_tail.next = n
        new_tail = new_tail.next
      if head == None:
        head = new_head
        tail = head
      else:
        tail.next = new_head
        tail = tail.next


    while lists != []:
      new_vals = findMins()
      addToLL(new_vals)
      removeVals(new_vals)

    return head

# Linked List 1: 1 -> 3 -> 7
node1_3 = ListNode(7)
node1_2 = ListNode(3, node1_3)
node1_1 = ListNode(1)

# Linked List 2: 2 -> 5 -> 9
node2_3 = ListNode(9)
node2_2 = ListNode(5, node2_3)
node2_1 = ListNode(2)

# Linked List 3: 4 -> 6 -> 8
node3_3 = ListNode(8)
node3_2 = ListNode(6, node3_3)
node3_1 = ListNode(4)

# Linked List 4: 3 -> 5 -> 10
node4_3 = ListNode(10)
node4_2 = ListNode(5, node4_3)
node4_1 = ListNode(3)

# 1 > 2 > 3 > 3 > 4 > 5 > 5 > 6 > 7 > 8 > 9 > 10

sol = Solution()
a = sol.mergeKLists([None, node1_1])


print_linked_list(a)

