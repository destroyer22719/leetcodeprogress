from typing import List

class Solution:
  def maxDistance(self, arrays: List[List[int]]) -> int:
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    same_arr = 0

    for i in range(len(arrays)):
      a = arrays[i]
      if a[0] < min_val and a[-1] > max_val:
        same_arr = i

        min_val = a[0]
        max_val = a[-1]
      elif a[0] < min_val and a[-1] <= max_val:
        same_arr = None
        min_val = a[0]
      elif a[-1] > max_val and a[0] >= min_val and i != 0:
        same_arr = None
        max_val = a[-1]
    
    if same_arr == None:
      return max_val - min_val
    
    dist = 0

    for i in range(len(arrays)):
      if i == same_arr:
        continue

      a = arrays[i]
      if a[-1] - min_val > dist:
        dist = a[-1] - min_val 
      if max_val - a[0] > dist:
        dist = max_val - a[0] 
    return dist
  
sol = Solution()
a = sol.maxDistance([[1,5],[3,4]])

print(a)