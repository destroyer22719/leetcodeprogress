from typing import List

class Solution:
  def maximumBeauty(self, nums: List[int], k: int) -> int:
    points = []

    for n in nums:
      points.append([n+k, "y"])
      points.append([n-k, "x"])
    points = sorted(points)

    result = 0
    count = 0
    for p in points:
      if p[1] == "x":
        count += 1
      else:
        count -= 1
      result = max(result, count)
    return result
  
sol = Solution()
a = sol.maximumBeauty([100000], 0)
print(a)