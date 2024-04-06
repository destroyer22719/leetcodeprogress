from typing import List


class Solution:
  def countBits(self, n: int) -> List[int]:
    result = [0]

    exp = 0
    for i in range(1, n+1):
      if (2**(exp+1))==i:
        exp += 1
        result.append(1) 
      else:
        result.append(result[i-2**(exp)]+1)
    return result
  
sol = Solution()
print(sol.countBits(8))