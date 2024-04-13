from typing import List


class Solution:
  def minimumDeletions(self, nums: List[int]) -> int:
    n = len(nums)
    mid = (n-1) // 2
    min_val = max_val = [nums[0],0]


    for i in range(1, n):
      if nums[i] > max_val[0]:
        max_val = [nums[i],i]
      if nums[i] < min_val[0]:
        min_val = [nums[i], i]
    
    def plan_a():
      left = min_val if max_val[1] > min_val[1] else max_val
      right = max_val if max_val[1] > min_val[1] else min_val

      return min(right[1] + 1, n - left[1])
    
    def plan_b():
      max_shift = min(max_val[1] + 1, n - max_val[1])
      min_shift = min(min_val[1] + 1, n - min_val[1])

      return max_shift + min_shift
    
    return min(plan_a(), plan_b())
  
sol = Solution()

answer = sol.minimumDeletions( [0,-4,19,1,8,-2,-3,5])
print(answer)