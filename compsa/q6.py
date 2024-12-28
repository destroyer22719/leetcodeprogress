from typing import List



class Solution:
   def firstMissingPositive(self, nums):
       n = len(nums)
      
       for i in range(n):
           while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
               # Swap nums[i] with nums[nums[i] - 1]
               nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
      
      
       for i in range(n):
           if nums[i] != i + 1:
               return i + 1
      


       return n + 1

    
sol = Solution()

a = sol.firstMissingPositive([7,8,9,11,12])
print(a)