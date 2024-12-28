from typing import List


class Solution:
  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    answer = []

    tracker = {}
    ranges = {}

    for q in queries:
      if q[0] not in ranges:
        ranges[q[0]] = {q[1]}
      else:
        ranges[q[0]].add(q[1])
    
    for start, nums in ranges.items():
      curr = arr[start]
      tracker[f"{start}:{start}"] = arr[start]
      for i in range(start+1, max(nums)+1):
        curr ^= arr[i]
        if i in nums:
          tracker[f"{start}:{i}"] = curr
    
    for q in queries:
      answer.append(tracker[f"{q[0]}:{q[1]}"])
    return answer
  
sol = Solution()
a = sol.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]])
print(a)

