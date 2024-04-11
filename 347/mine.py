from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counts = {}

    for n in nums:
      if n not in counts:
        counts[n] = 1
      else:
        counts[n] += 1
    
    print(counts)
    return [key for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True)][:k]
  
sol = Solution()

sol = sol.topKFrequent([4,1,-1,2,-1,2,3], 2)
print(sol)