from typing import List


class Solution:
  def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    curr_location = [0, 0]

    direction = 1/2
    max_distance = 0

    def turn(dir):
      nonlocal direction

      if dir == -1:
        direction -= 1/2
      elif dir == -2:
        direction += 1/2
      
      direction = direction % 2
      if direction < 0:
        direction = 2 + direction

    obstacles_manager = {
      0: {},
      1: {}
    }

    for o in obstacles:
      if o[0] not in obstacles_manager[0]:
        obstacles_manager[0][o[0]] = [o[1]]
      else:
        obstacles_manager[0][o[0]].append(o[1])

      if o[1] not in obstacles_manager[1]:
        obstacles_manager[1][o[1]] = [o[0]]
      else:
        obstacles_manager[1][o[1]].append(o[0])

    
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

      if new_loc[(1+index) % 2] not in obstacles_manager[(1+index) % 2]:
        new_loc[index] += coefficient*c
      else:
        changed = False
        for o in obstacles_manager[(1+index) % 2][new_loc[(1+index) % 2]]:
          if (coefficient == 1 and new_loc[index] < o and o < new_loc[index] + coefficient*c):
            changed = True
            new_loc[index] = o - 1
            break
          elif (coefficient == -1 and new_loc[index] + coefficient*c < o and o < new_loc[index]):
            changed = True
            new_loc[index] = o + 1
            break
        if not changed:
          new_loc[index] += coefficient*c
      curr_location = new_loc
      max_distance = max(max_distance, curr_location[0]**2 + curr_location[1]**2)
    return max_distance

sol = Solution()
a = sol.robotSim([7,-2,-2,7,5], [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]])
print(a)