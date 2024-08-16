from typing import List

class Solution:
  def validPartition(self, nums: List[int]) -> bool:
    found = False

    def dp(arr):
      nonlocal found

      if found or len(arr) == 1:
        return
      
      if len(arr) == 0:
        found = True
        return
      
      if arr[0] == arr[1]:
        dp(arr[2:])
      if len(arr) >= 3:
        if arr[0] == arr[1] and arr[1] == arr[2]:
          dp(arr[3:])
        elif arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
          dp(arr[3:])

    dp(nums)
    return found