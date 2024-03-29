class Solution(object):
  def containsDuplicate(self, nums):
    prev = {}

    for n in nums:
      if n in prev:
        return True
      prev[n] = True
    return False

answer = Solution()

isDuplicate = answer.containsDuplicate([1,1,2,3,5])