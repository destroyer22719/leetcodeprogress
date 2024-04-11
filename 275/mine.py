from typing import List


class Solution:
  def hIndex(self, citations: List[int]) -> int:
    curr_h = 0

    l,r = 0, len(citations) - 1
    n = len(citations)

    if n == 1:
      return 1 if citations[0] >= 1 else 0

    while l <= r:
      i = (l + r) // 2

      if citations[i] == (n - i):
        return citations[i]
      if citations[i] > (n - i):
        r = i - 1
        curr_h = n - i
      else:
        l = i + 1
    return curr_h
  
sol = Solution()

answer = sol.hIndex([0,1])
print(answer)


      