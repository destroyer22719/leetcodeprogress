class Solution:
  def findTargetSumWays(self, nums, target):
    dp = {}

    def backtrack(i, total):
      if i == len(nums):
        return 1 if total == target else 0
      if (i, total) in dp:
        return dp[(i, total)]
      if total + sum(nums[i:]) < target or total - sum(nums[i:]) > target:
        return 0
      dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
      return dp[(i, total)]
    answer =  backtrack(0, 0)
    return answer
  
print(Solution().findTargetSumWays([1,1,1], 3))