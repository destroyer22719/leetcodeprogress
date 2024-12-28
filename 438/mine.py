from typing import List

class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    tracker = {}
    curr = {}

    for i in p:
      tracker[i] = tracker.get(i, 0) + 1
    
    q = []
    answer = []

    for i in range(len(s)):
      l = s[i]

      q.append(l)
      curr[l] = curr.get(l, 0) + 1

      if len(q) > len(p):
        first = q[0]
        
        curr[first] -= 1
        if curr[first] == 0:
          del curr[first]
        q.pop(0)

      if len(q) == len(p) and tracker == curr:
        answer.append(i + 1 - len(p))
    return answer

sol = Solution()
a = sol.findAnagrams("cbaebabacd", "abc")
print(a)
      