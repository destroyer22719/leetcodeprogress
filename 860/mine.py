from typing import List

class Solution:
  def lemonadeChange(self, bills: List[int]) -> bool:
    change = {
      5: 0,
      10: 0,
      20: 0,
    }

    for b in bills:
      if b == 5:
        change[5] += 1
      elif b == 10:
        if change[5] < 1:
          return False
        change[5] -= 1
        change[10] += 1
      elif b == 20:
        if (change[5] > 0 and change[10] > 0):
          change[5] -= 1
          change[10] -= 1
          change[20] += 1
        elif change[5] > 2:
          change[5] -= 3
          change[20] += 1
        else:
          return False
    return True

sol = Solution()
print(sol.lemonadeChange([5,5,5,10,20]))