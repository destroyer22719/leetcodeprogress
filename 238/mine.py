class Solution(object):
  def productExceptSelf(self, nums):
    hasZeros = False
    totalProduct = 1

    for n in nums:
      if n == 0:
        # If it has multiple zeros, then it's an array full of zeros as the answer
        if hasZeros == True:
          return [0]*len(nums)
        else:
          hasZeros = True
          continue
      else:
        totalProduct *= n
    
    answer = []
    for n in nums:
      if hasZeros == True:
        if n == 0:
          answer.append(totalProduct)
        else:
          answer.append(0)
      else:
        answer.append(totalProduct/n)
    return answer
    
sol = Solution()

answer = sol.productExceptSelf([-1,1,0,-3,3])
print(answer)