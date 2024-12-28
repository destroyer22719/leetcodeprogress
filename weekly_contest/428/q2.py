from typing import List

class Solution:
  def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
    # Check if we can convert back to initial currency
    found = False
    for p in pairs2:
      if initialCurrency in p:
        found = True
        break
    
    if not found:
      return 1.0
    
    answer = 1.0
    visited = {}

    def dfs(currentCurr, amt, day, prevCurr):
      nonlocal answer
      nonlocal visited

      if f"{day}-{prevCurr}-{currentCurr}-{amt}" in visited:
        return
      visited[f"{day}-{prevCurr}-{currentCurr}-{amt}"] = True

      if currentCurr == initialCurrency and answer < amt:
        answer = amt

      if day == 1:
        for i in range(len(pairs1)):
          p = pairs1[i]
          if currentCurr == p[0]:
            dfs(p[1], amt * rates1[i], 1, currentCurr)
          elif currentCurr == p[1]:
            dfs(p[0], amt / rates1[i], 1, currentCurr)
      for i in range(len(pairs2)):
        p = pairs2[i]
        if currentCurr == p[0]:
          dfs(p[1], amt * rates2[i], 2, currentCurr)
        elif currentCurr == p[1]:
          dfs(p[0], amt / rates2[i], 2, currentCurr)
    
    for i in range(len(pairs1)):
      p = pairs1[i]
      if initialCurrency == p[0]:
        dfs(p[1], 1 * rates1[i], 1, initialCurrency)
      elif initialCurrency == p[1]:
        dfs(p[0], 1 / rates1[i], 1, initialCurrency)
    return answer
  
sol = Solution()
a = sol.maxAmount("NGN", [["NGN","EUR"]], [9.0], [["NGN","EUR"]], [6.0])

print(a)