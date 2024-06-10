from typing import List

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    rows = len(board)
    cols = len(board[0])

    def isValidA(y_n, x_n):
      if y_n < 0 or x_n < 0 or y_n >= rows or x_n >= cols:
        return False
      return True

    def isValidB(y_n, x_n, path, visited):
      if [y_n, x_n] in visited or board[y_n][x_n] != word[len(path) - 1]:
        return False
      return True
    
    def search(y, x, path=[], visited=[]):
      neighbours = [[y-1, x], [y+1, x], [y,x-1], [y,x+1]]

      if "".join(path) == word:
        return True

      for n in neighbours:
        if isValidA(n[0], n[1]) and isValidB(n[0], n[1], list(path + [board[n[0]][n[1]]]), list(visited)) and search(n[0], n[1], list(path + [board[n[0]][n[1]]]), list(visited + [n])):      
          return True          
      return False

    letters_found = []

    for i in range(rows):
      for j in range(cols):
        if board[i][j] in word and board[i][j] not in letters_found:
          letters_found.append(board[i][j])
    
    if len(letters_found) != len(list(set(word))):
      return False

    for i in range(rows):
      for j in range(cols):
        if board[i][j] == word[0]:
          if search(i, j, [board[i][j]], [[i,j]]):
            return True
    return False
  
sol = Solution()
a = sol.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAa")
print(a)