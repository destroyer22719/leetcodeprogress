from typing import List

class Solution:
  def minDays(self, grid: List[List[int]]) -> int:
    size = 0
    count = 0

    def dfs(i, j):
      nonlocal size
      if i < 0 or  i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return
      
      size += 1
      grid[i][j] = 2

      dfs(i - 1, j)
      dfs(i + 1, j)
      
      dfs(i, j - 1)
      dfs(i, j + 1)

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1:
          size = 0
          dfs(i, j)
          count += 1

    if count > 1:
      return 0
    if size == 2:
      return 2
    
    min_x = {i:0 for i in range(len(grid))}
    curr_x = {i:0 for i in range(len(grid))}

    min_y = {i:0 for i in range(len(grid[0]))}
    curr_y = {i:0 for i in range(len(grid[0]))}

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] != 0:
          curr_x[i] += 1
          curr_y[j] += 1
        else:
          min_x[i] = max(min_x[i], curr_x[i])
          min_y[j] = max(min_y[j], curr_y[i])

          curr_x[i] = curr_y[j] = 0
    
    values = list(min_x.values()) + list(min_y.values())
    result = None

    for v in values:
      if v != 0 and (result == None or v < result):
        result = v
      
    return result

sol = Solution()
print(sol.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))
