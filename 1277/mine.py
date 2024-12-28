from typing import List

class Solution:
  def countSquares(self, matrix: List[List[int]]) -> int:
    sizes = {}
    total = 0

    def mark_square(i, j):
      size = 1
      if i == len(matrix) - 1 or j == len(matrix[0]) - 1:
        matrix[i][j] = -1
      else:
        # for w in range(1, min(len(matrix) - i, len(matrix[0]) - j)):
        #   for x in range(w):
        #     for y in range(w):
        #       if matrix[i+x][j+y] != 1 or matrix[i+y][j+x] != 1:
        #         break
        #     else:
        #       continue
        #     break
        #   else:
        #     size += 1
        #     continue
        #   break
        for x in range(1, min(len(matrix) - i, len(matrix[0]) - j)):
          for y in range(x+1):
            if matrix[i+x][j+y] != 1 or matrix[i+y][j+x] != 1:
              break
          else:
            size += 1
            continue
          break
          

        # while size < min(len(matrix) - i, len(matrix[0]) - j):
        #   if matrix[i + size][j] != 1 or matrix[i][j + size] != 1:
        #     break
        #   size += 1

        # for x in range(size):
        #   matrix[i + x][j] = -1
        #   matrix[i][j + x] = -1
        for x in range(size):
          for y in range(size):
            matrix[i+x][j+y] = -1
            matrix[i+y][j+x] = -1
      return size

    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
          curr_size = mark_square(i,j)
          sizes[curr_size] = sizes.get(curr_size, 0) + 1
    
    dp = [0]

    if len(sizes) == 0:
      return 0
    
    for size in range(1, max(sizes.keys()) + 1):
      squares = dp[size - 1] + size**2
      dp.append(squares)

      total += squares*sizes.get(size, 0)
    return total
  
sol = Solution()
print(sol.countSquares(
[[1,0,1,0,1],[1,0,0,1,1],[0,1,0,1,1],[1,0,0,1,1]]
))
