from typing import List

class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    odds = []    

    for i in range(len(nums)):
      if nums[i] % 2 == 1:
        odds.append(i)

    count = 0
    for start in range(len(odds) - k + 1):
      stop = start + k - 1

      prev = -1 if start == 0 else odds[start - 1]
      next = len(nums) if stop + 1 > len(odds) - 1 else odds[stop + 1]

      left = max(odds[start] - prev - 1, 0)
      right = max(next - odds[stop] - 1, 0)

      if left > 0:
        left += 1
      if right > 0:
        right += 1


      if left == 0 and right == 0:
        count += 1
      if left == 0 or right == 0:
        count += right + left
      else:
        count += right*left
    return count
     
  
sol = Solution()
a = sol.numberOfSubarrays([2044,96397,50143], 1)
print(a)

a = sol.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)
print(a)

a = sol.numberOfSubarrays([1,1,1,1,1], 1)
print(a)