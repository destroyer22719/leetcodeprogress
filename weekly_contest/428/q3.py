from typing import List

class Solution:
  def beautifulSplits(self, nums: List[int]) -> int:
    total = 0

    if len(nums) < 3:
      return total
    
    #find where num1 is a prefix of num2
    
    def find(n):
      nonlocal total
      s = "".join(map(str, n))

      for i in range(1, (len(n) // 2) + 1):
        num1 = "".join(map(str, n[:i]))
        if num1 == s[i:i+i]:
          total += max(len(n) - i - 1,1)
        
    
    # find where nums1 is a prefix of nums2
    find(nums)

    # find where nums2 is a prefix of nums3
    for i in range(1, len(nums) - 1):
      find(nums[i:])
    return total
  
sol = Solution()
a = sol.beautifulSplits([1,1,0,1,3,2,2,2])

print(a)