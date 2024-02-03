class Solution:
  def findTargetSumWays(self, nums, target):
    results = []
    arraySum = sum(nums)

    for i in range(len(nums)):
      if i == 0:
        results.append([[1], nums[i]])
        results.append([[-1], -nums[i]])
      else:
        for j in range(len(results)):
          r = results[j]

          new_results = list(results)

          if r[1] + sum(nums[i:]) >= target:
            new_results.append([r[0] + [1], r[1] + nums[i]])
            new_results.append([r[0] + [-1], r[1] - nums[i]])
          results = new_results
    return len([r for r in results if r[1] == target and len(r[0])==len(nums)])
  
print(Solution().findTargetSumWays([1,1,1], 3))