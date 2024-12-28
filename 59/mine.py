from typing import List

class Solution:
  def generateMatrix(self, n: int) -> List[List[int]]:
    top = 0
    bot = n

    left = 0
    right = n

    curr = 1

    result = []
    for i in range(n):
      row = []
      for j in range(n):
        row.append(0)
      result.append(row)
    
    while top < bot and left < right:
      for i in range(left, right):
        result[top][i] = curr
        curr += 1
      top += 1

      for i in range(top, bot):
        result[i][right - 1] = curr
        curr += 1
      right -= 1

      for i in range(right - 1, left -1, -1):
        result[bot - 1][i] = curr
        curr += 1
      bot -= 1

      for i in range(bot - 1, top - 1, -1):
        result[i][left] = curr
        curr += 1
      left += 1
    return result
  
sol = Solution()
a = sol.generateMatrix(3)
print(a)