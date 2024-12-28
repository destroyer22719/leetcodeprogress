def funcHopSkipJump(matrix):
  turn = [[0,0]]
  curr_index = [0, 0]

  visited = {"(-1, -1)"}

  def isValid(i, j):
    nonlocal matrix
    nonlocal visited

    if (i, j) in visited:
      return False
    if i < 0 or i > len(matrix) - 1:
      return False
    if j < 0 or j > len(matrix[0]) - 1:
      return False

    return True

  def move(i, j):
    nonlocal curr_index
    nonlocal visited
    nonlocal turn

    curr_index[0] = i
    curr_index[1] = j

    visited.add((i, j))
    turn.append(list(curr_index))

  while True:
    if isValid(curr_index[0] - 1, curr_index[1]):
      move(curr_index[0] - 1, curr_index[1])
    elif isValid(curr_index[0], curr_index[1] - 1):
      move(curr_index[0], curr_index[1] - 1)
    elif isValid(curr_index[0] + 1, curr_index[1]):
      move(curr_index[0] + 1, curr_index[1])
    elif isValid(curr_index[0], curr_index[1] + 1):
      move(curr_index[0], curr_index[1] + 1)
    else:
      break

  if len(turn) % 2 == 0:
    i = turn[-1][0]
    j = turn[-1][1]

  else:
    i = turn[-1][0]
    j = turn[-1][1]

  return matrix[i][j]

funcHopSkipJump([
  [9, 8, 7, 6],
  [5,4,3,2],
  [1, 10, 11, 12]
])