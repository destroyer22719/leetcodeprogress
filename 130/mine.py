from typing import List

class Solution:
  def infect(self, y,x):
    if self.original[y][x] == "O":
      print(y, x)
      self.result[y][x] = "O"

      if self.valid_coords(y + 1, x):
        self.infect(y + 1, x)
      if self.valid_coords(y, x + 1):
        self.infect(y, x + 1)
      if self.valid_coords(y - 1, x):
        self.infect(y - 1, x)
      if self.valid_coords(y, x - 1):
        self.infect(y, x - 1)

  def valid_coords(self, y, x):
    within_bounds = (x < self.w and y < self.h) and (0 <= x and 0 <= y)

    if not within_bounds:
      return False

    return self.result[y][x] == "X" and self.original[y][x] == "O"
  

  def solve(self, board: List[List[str]]) -> None:
    self.h = len(board)
    self.w = len(board[0])

    self.original = board
    # self.result = [["X"]*self.w]*self.h

    self.result = [["X" for _ in range(self.w)] for _ in range(self.h)]

    # self.result[0][0] = "O"

    for i in range(self.h):
      if self.original[i][0] == "O":
        self.infect(i, 0)
      if self.original[i][self.w-1] == "O":
        self.infect(i, self.w-1) == "O"

    for j in range(self.w):
      if self.original[0][j] == "O":
        self.infect(0, j)
      if self.original[self.h-1][j] == "O":
        self.infect(self.h-1, j)

    return self.result
  
sol = Solution()
answer = sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
print(answer)