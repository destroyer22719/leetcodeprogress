from typing import List

class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    max_num = max(nums)

    max_cont = 1
    curr = 0
    for n in nums:
      if n == max_num:
        curr += 1
      else:
        max_cont = max(max_cont, curr)
        curr = 0
    return max(max_cont, curr)

sol = Solution()
a = sol.longestSubarray([378034,378034,378034])
print(a)