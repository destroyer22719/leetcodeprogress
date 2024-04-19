from typing import List

class Solution:
  def wiggleSort(self, nums: List[int]) -> None:
    sorted_ver = sorted(nums)

    if len(nums) <= 2:
      for i in range(len(nums)):
        nums[i] = sorted_ver[i]
      return

    mid = len(nums) // 2

    lower_half = sorted_ver[:mid]
    upper_half = sorted_ver[mid:]

    while True:
      if (len(upper_half) > len(lower_half)):
        lower_half.append(upper_half[0])
        upper_half.pop(0)
      else:
        break

    l_i = 0
    u_i = 0

    for i in range(len(nums)):
      if (i % 2) == 0:
        nums[i] = lower_half[l_i]
        l_i += 1
      else:
        nums[i] = upper_half[u_i]
        u_i += 1
    print(nums)

sol = Solution()

# sol.wiggleSort([1,3,2,2,3,1])
# sol.wiggleSort([1,1,2,1,2,2,1])
# sol.wiggleSort([1,2,3])
nums = [2,1]
sol.wiggleSort(nums)
print(nums)