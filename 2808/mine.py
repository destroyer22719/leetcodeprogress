from typing import List
from collections import Counter

class Solution:
  def minimumSeconds(self, nums: List[int]) -> int:
    result = 0
    n = len(nums)
    
    while True:
      tracker = dict(Counter(nums))
      prev_val = {}
      distance = {}

      if len(tracker) == 1:
        return result

      for i in range(len(nums)):
        if nums[i] not in prev_val:
          prev_val[nums[i]] = i
          distance[nums[i]] = 0
        else:
          distance[nums[i]] += i - prev_val[nums[i]] - 1
          prev_val[nums[i]] = i

      new = list(nums)
      for i in range(len(nums)):
        a = (i + 1) % n
        b = (i - 1) % n

        possible_values = [nums[a], nums[b], nums[i]]
        max_key = max(possible_values, key=lambda k: tracker[k])
        ties = [k for k in possible_values if tracker[k] == tracker[max_key]]

        if len(ties) > 1:
          new[i] = nums[max(ties, key=lambda k: distance[k])]
        else:
          new[i] = nums[max_key]
      nums = new
      result += 1
  
sol = Solution()
a = sol.minimumSeconds([1,2,1,2])
print(a)