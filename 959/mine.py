from typing import List

class Solution:
  def regionsBySlashes(self, grid: List[str]) -> int:
    result = 0
    newgrid = [ [" " for _ in range(len(grid[0]*2))] for _ in range(len(grid)*2)]

    def dfs(i, j):
      nonlocal result

      if i < 0 or i >= len(newgrid) or j < 0 or j >= len(newgrid[0]) or newgrid[i][j] != " ":
        return
      
      newgrid[i][j] = result

      dfs(i - 1, j)
      dfs(i + 1, j)

      dfs(i, j - 1)
      dfs(i, j + 1)

      if i + 1 < len(newgrid) and j + 1 < len(newgrid[0]) and (newgrid[i+1][j] != "/" and newgrid[i][j+1] != "/"):
        dfs(i+1, j+1)
      if i - 1 >= 0 and j - 1 >= 0 and newgrid[i-1][j] != "/" and newgrid[i][j-1] != "/":
        dfs(i-1, j-1)
      if j - 1 >= 0 and i + 1 < len(newgrid) and newgrid[i+1][j] != "\\" and newgrid[i][j-1] != "\\":
        dfs(i+1, j-1)
      if j + 1 < len(newgrid[0]) and i - 1 >= 0 and newgrid[i-1][j] != "\\" and newgrid[i][j+1] != "\\":
        dfs(i-1, j+1)

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == "/":
          newgrid[i*2][j*2+1] = " /"
          newgrid[i*2+1][j*2] = "/"
        elif grid[i][j] == "\\":
          newgrid[i*2][j*2] = "\\"
          newgrid[i*2+1][j*2+1] = "\\"

    for i in range(len(newgrid)):
      for j in range(len(newgrid[0])):
        if newgrid[i][j] == " ":
          result += 1
          dfs(i, j)

    return result

s = Solution()

print(s.regionsBySlashes(["//","/ "]))
