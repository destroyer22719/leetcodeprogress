from typing import List
import math

class Solution:
  def largestCombination(self, candidates: List[int]) -> int:
    byte_size = int(math.ceil(math.log2(max(candidates))))

    def get_binary(num, byte_size):
      result = []
      for i in range(byte_size, -1, -1):
        if 2**i <= num:
          result.append(1)
          num -= 2**i
        else:
          result.append(0)
      return result
    
    binaries = []
    for num in candidates:
      binaries.append(get_binary(num, byte_size))
    
    result = 1
    for i in range(len(binaries[0])):
      total = 0
      for j in binaries:
        total += j[i]
      result = max(result, total)
    return result
  
sol = Solution()
a = sol.largestCombination([33,93,31,99,74,37,3,4,2,94,77,10,75,54,24,95,65,100,41,82,35,65,38,49,85,72,67,21,20,31])
print(a)