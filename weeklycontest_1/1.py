from typing import List


class Solution:
  def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
    curr_pos = 0

    while commands != []:
      if commands[0] == "UP":
        curr_pos -= n
      if commands[0] == "DOWN":
        curr_pos += n
      if commands[0] == "RIGHT":
        curr_pos += 1
      if commands[0] == "LEFT":
        curr_pos -= 1

      commands.pop(0)
    return curr_pos