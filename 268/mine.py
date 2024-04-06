from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    remainder = (n*(n+1))/2

    for num in nums:
      remainder -= num
    return remainder