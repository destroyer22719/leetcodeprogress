class Solution:
  def minimumOperations(self, nums: List[int]) -> int:
    result = 0

    while len(set(nums)) != len(nums):
      nums = nums[3:]
      result += 1
    return result