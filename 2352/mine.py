from typing import List


class Solution:
  def equalPairs(self, grid: List[List[int]]) -> int:
    n = len(grid)

    values = {}
    result = 0
    columns = [""] * n

    for i in range(n):
      row = ""
      for j in range(n):
        row += f"{grid[i][j]}-"

        columns[j] += f"{grid[i][j]}-"

      if row in values:
        values[row] += 1
      else:
        values[row] = 1

    for c in columns:
      if c in values:

        result += values[c]
    
    return result
  
sol = Solution()
a = sol.equalPairs([[11,1],[1,11]])
# a = sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
print(a)
      