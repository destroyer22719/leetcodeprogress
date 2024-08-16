from typing import List

class Solution:
  def missingElement(self, nums: List[int], k: int) -> int:
    remaining = k
    curr = None

    for i in range(1, len(nums)):
      if nums[i] != nums[i-1] + 1:
        for j in range(nums[i-1] + 1, nums[i]):
          curr = j
          remaining -= 1

          if remaining == 0:
            return curr
          
    return nums[-1] + remaining

sol = Solution()

a = sol.missingElement([4,7,9,10], 1)
print(a)