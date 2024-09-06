from typing import List


class Solution:
  def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    curr_location = [0, 0]

    direction = 1/2
    max_distance = 0

    obstacles = {tuple(o) for o in obstacles}

    def turn(dir):
      nonlocal direction

      if dir == -1:
        direction -= 1/2
      elif dir == -2:
        direction += 1/2
      
      direction = direction % 2
      if direction < 0:
        direction = 2 + direction

    for c in commands:
      new_loc = list(curr_location)

      if c == -1 or c == -2:
        turn(c)
        continue

      index = 1
      coefficient = 1

      if direction == 1/2 or direction == 3/2:
        index = 1
      else:
        index = 0
      if direction == 3/2 or direction == 1:
        coefficient = -1

      for _ in range(c):
        new_loc[index] += coefficient

        if new_loc in obstacles:
          new_loc[index] -= coefficient
          break
        curr_location = new_loc
      max_distance = max(max_distance, curr_location[0]**2 + curr_location[1]**2)
    return max_distance