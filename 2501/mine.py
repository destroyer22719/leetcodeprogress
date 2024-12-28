from typing import List

class Solution:
  def longestSquareStreak(self, nums: List[int]) -> int:
    highest_streak = -1

    nums = sorted(list(set(nums)))
    next_squares = {}

    for n in nums:
      if n in next_squares:
        next_squares[n**2] = next_squares[n] + 1
        highest_streak = max(highest_streak, next_squares[n] + 1)
      else:
        next_squares[n**2] = 1
    return highest_streak