from typing import List


class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    sumOfPairs = {}

    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        sum = nums[i]+nums[j]
        sumOfPairs[sum] =sumOfPairs.get(sum, [])
        sumOfPairs[sum].append([i, j])
    
    solutions = []

    for i in range(len(nums)):
      if (-nums[i] in sumOfPairs):
        for pairs in sumOfPairs[-nums[i]]:
          if (i in pairs):
            continue

          answer = [] + [nums[pairs[0]]] + [nums[pairs[1]]] + [nums[i]]

          answer = sorted(answer)

          if answer not in solutions:
            solutions.append(answer)

    return solutions

sol = Solution()

print(sol.threeSum([-1,0,1,2,-1,-4]))