from typing import Optional

class Node:
  def __init__(self, val=0, neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    cloned = {}

    def dfs(n):
      if n.val in cloned:
        return
      
      cp = Node(n.val, [])
      cloned[n.val] = cp

      for neighbor in n.neighbors:
        if neighbor.val not in cloned:
          dfs(neighbor)

        cloned[n.val].neighbors.append(cloned[neighbor.val])

    if node is None:
      return None
    dfs(node)

    return cloned[node.val]

def print_adjacency_list(node):
    if not node:
        return
    
    visited = {}
    queue = [node]
    
    while queue:
        curr = queue.pop(0)
        
        if curr in visited:
            continue
        
        # Print the current node's value and its neighbors' values
        neighbors_vals = [neighbor.val for neighbor in curr.neighbors]
        print(f'{curr.val}: {neighbors_vals}')
        
        visited[curr] = neighbors_vals
        
        # Add unvisited neighbors to the queue
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)



# Create the nodes manually
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

# Manually set up the neighbors according to the given edges
# Edge [2, 4]
n1.neighbors.append(n4)
n1.neighbors.append(n2)

# Edge [1, 3]
n2.neighbors.append(n1)
n2.neighbors.append(n3)

n3.neighbors.append(n2)
n3.neighbors.append(n4)

n4.neighbors.append(n1)
n4.neighbors.append(n3)



sol = Solution()
answer = sol.cloneGraph(n1)
print(answer)

print_adjacency_list(answer)