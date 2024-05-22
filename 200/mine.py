from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    count = 2
    rows = len(grid)
    cols = len(grid[0])

    def isValid(y, x):
      return not (x < 0 or x >= cols or y < 0 or y >= rows or int(grid[y][x]) == 0 or int(grid[y][x]) > 1)

    def dfs(y,x):
      if not isValid(y, x):
        return
      
      grid[y][x] = count

      dfs(y, x-1)
      dfs(y, x+1)
      dfs(y-1, x)
      dfs(y+1, x)
    
    for i in range(rows):
      for j in range(cols):
        if isValid(i, j):
          count += 1
          dfs(i, j)

    return count - 2

sol = Solution()

answer = sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])

print(answer)
