from typing import List

class Solution:
  def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
    prefexes = {}

    arr1 = sorted(list(set(arr1)), reverse=True)
    arr2 = sorted(list(set(arr2)), reverse=True)

    longest = arr1 if len(arr1) >= len(arr2) else arr2
    shortest = arr1 if len(arr1) < len(arr2) else arr2

    for num in longest:
      numStr = str(num)

      if (numStr in prefexes):
        continue

      for i in range(1, len(numStr)+1):
        if numStr[:i] not in prefexes:
          prefexes[numStr[:i]] = i
    
    answer = 0

    for num in shortest:
      numStr = str(num)

      if len(numStr) < answer:
        continue

      for i in range(1, len(numStr) + 1):
        if numStr[:i] in prefexes and prefexes[numStr[:i]] > answer:
          answer = prefexes[numStr[:i]]
    
    return answer
  
sol = Solution()

# answer = sol.longestCommonPrefix([1,10,100], [1000])
# print(answer) 

answer = sol.longestCommonPrefix([10], [17, 11])
print(answer)