from typing import List

class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])

    rows = {}
    cols = {}

    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          if i not in rows:
            rows[i] = True
          if j not in cols:
            cols[j] = True
    
    for i in range(max(m, n)):
      if i < n:
        for r in rows:
          matrix[r][i] = 0
      if i < m:
        for c in cols:
          matrix[i][c] = 0
    
sol = Solution()
m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(m)
print(m)
