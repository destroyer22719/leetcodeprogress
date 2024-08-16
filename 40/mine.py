from typing import List


class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates = sorted(candidates)
    def dfs(allowed, path, total):
      if total == target:
        result.append(path)
        return
      if allowed == []:
        return
      for i in range(len(allowed)):
        if total + allowed[i] <= target and  (i == 0 or allowed[i] != allowed[i-1]):
          dfs(allowed[i+1:], path + [allowed[i]], total + allowed[i])
      
    dfs(candidates, [], 0)
    return result

sol = Solution()
print(sol.combinationSum2([1,2,7,6,1,5], 8))