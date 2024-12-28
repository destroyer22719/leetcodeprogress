from typing import List

class Solution:
  def maxDistinctElements(self, nums: List[int], k: int) -> int:
    if k == 0:
      return len(set(nums))
    
    nums = sorted(nums)
    new = [nums[0] - k]

    for i in range(1, len(nums)):
      if nums[-1] + k < new[-1]:
        break 
      if nums[i] + k < new[-1]:
        continue
      elif nums[i] != nums[i-1]:
        if nums[i] - k > new[-1]:
          new.append(nums[i] - k)
        else:
          new.append(new[-1] + 1)
      else:
        if new[-1] + 1 > nums[i] + k:
          continue
        else:
          new.append(new[-1] + 1)
    return len(new)
  
sol = Solution()
a = sol.maxDistinctElements([6,6,6,7,7], 1)
print(a)