from typing import List

class Solution:
  def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    data = sorted(zip(difficulty, profit))
    total = 0
    worker = sorted(worker)
    prev = None

    for i in range(len(worker)):
      
      for j in range(prev or 0, len(data)):
        if worker[i] < data[j][0]:
          break
        if prev == None or data[prev][1] < data[j][1]:
          prev = j
      if prev != None:
        total += data[prev][1]
    return total

class Solution:
  def maxProfitAssignment(self, d: List[int], profit: List[int], worker: List[int]) -> int:
    jobs = sorted(zip(d, profit))
    worker.sort()

    ans = j = maxp = 0

    for w in worker:
      while j < len(jobs) and jobs[j][0] <= w:
          maxp = max(maxp, jobs[j][1])
          j += 1
      ans += maxp
    return ans

sol = Solution()
a = sol.maxProfitAssignment([2, 4, 6], [10, 20, 30], [3, 4, 5])

print(a)
    