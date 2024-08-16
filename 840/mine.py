from typing import List


class Solution:
  def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    if len(grid) < 3 or len(grid[0]) < 3:
      return 0
    

    r1 = r2 = r3 = []
    c1 = [] 
    c2 = []
    c3 = []

    results = 0


    for i in range(len(grid) - 2):
      c1 = [] 
      c2 = []
      c3 = []

      for x in range(3):
        c1.append(grid[x+i][0])
        c2.append(grid[x+i][1])
        c3.append(grid[x+i][2])

      r1 = grid[i][0:3]
      r2 = grid[i+1][0:3]
      r3 = grid[i+2][0:3]

      for j in range(len(grid[0]) - 2):
        if j != 0:
          c3, c2, c1 = [x[j+2] for x in grid[i:i+3]], c3, c2
          r1.pop(0)
          r1.append(grid[i][j+2])

          r2.pop(0)
          r2.append(grid[i+1][j+2])

          r3.pop(0)
          r3.append(grid[i+2][j+2])
        
        if len(set(c1)) != 3 or len(set(c2)) != 3 or len(set(c3)) != 3 or len(set(r1)) != 3 or len(set(r2)) != 3 or len(set(r3)) != 3\
          or max(c1) > 9 or max(c2) > 9 or max(c3) > 9 or min(c1) < 1 or min(c2) < 1 or min(c3) < 1:
          continue

        if sum(r1) == sum(r2) and sum(r2) == sum(r3) and sum(c1) == sum(c2) and sum(c2) == sum(c3) and sum(c3) == sum(r3) and (r1[0] + r2[1] + r3[2]) == sum(r3):
          results += 1

    return results
    

sol = Solution()
a = sol.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]])
print(a)