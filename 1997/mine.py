from typing import List


class Solution:
  def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
    visited_count = {}

    curr_rm = nextVisit[0]
    curr_day = 0

    while True:
      if len(nextVisit) == len(list(visited_count.keys())):
        return curr_day - 1

      if curr_rm not in visited_count:
        visited_count[curr_rm] = 1
        curr_rm = nextVisit[curr_rm]
      else:
        visited_count[curr_rm] += 1
        if visited_count[curr_rm] % 2 == 1:
          curr_rm = nextVisit[curr_rm]
        else:
          curr_rm = (curr_rm + 1) % len(nextVisit)

      curr_day += 1 
      
sol = Solution()

result = sol.firstDayBeenInAllRooms([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

print(result)