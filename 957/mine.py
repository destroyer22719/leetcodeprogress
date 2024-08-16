from typing import List

class Solution:
  def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
    tracker = [cells]
    

    for i in range(1, n + 1):
      curr_date = [0]*8

      for j in range(1, 7):
        if tracker[-1][j-1] == tracker[-1][j+1]:
          curr_date[j] = 1
      
      if curr_date in tracker:
        index = tracker.index(curr_date)

        answer_index = n % (len(tracker) - index)
        
        return tracker[answer_index + (1 if len(tracker) == 2 else 0)]
      elif i == n:
        return curr_date
      tracker.append(curr_date)

sol = Solution()

a = sol.prisonAfterNDays([1,1,0,1,1,0,0,1], 300663720)

print(a)

a = sol.prisonAfterNDays([1,1,0,1,1,0,1,1], 6)

print(a)