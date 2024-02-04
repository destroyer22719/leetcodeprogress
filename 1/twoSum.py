class Solution(object):
  def twoSum(self, nums, target):
    n = len(nums)

    # prevCalcs = {}

    for i in range(n):
      for j in range(i + 1, n):
        if i == j:
          continue
        
        # arr = [i,j]
        # arr.sort()
        # index = "".join(str(x) for x in arr)
        # if index in prevCalcs:
        #   continue
        
        if nums[i] + nums[j] == target:
          return [i, j]
        
        # prevCalcs[index] = nums[i] + nums[j]

myClass = Solution()

answer = myClass.twoSum([2,7,11,15], 9)
print(answer)