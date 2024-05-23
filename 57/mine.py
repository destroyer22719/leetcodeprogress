from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    sol = []

    if intervals == []:
      return [newInterval]
    
    if len(intervals) ==  1:
      return [min(newInterval[0], intervals[0][0]), max(newInterval[1], intervals[0][1])]

    for i in range(1, len(intervals)):
      a = intervals[i - 1]
      b = intervals[i]

      if a[1] < newInterval[0] and b[0] > newInterval[1]:
        sol.append(a)
        sol.append(newInterval)
        sol.append(b)

        return sol + intervals[i + 1]
      if i == len(intervals) - 1:
        return 
      elif b[1] < newInterval[0] or a[0] > newInterval[0]:
        sol.append(a)
        sol.append(b)
      else:
        solInt = []
        if a[1] < newInterval[0]:
          sol.append(a)
          solInt = [b[0]]
        else:
          solInt = [a[0]]
          

        for j in range(i-1, len(intervals)):
          if intervals[j][1] > newInterval[1]:
            solInt.append(intervals[j][1])
            sol.append(solInt)
            return sol + intervals[j+1:]
          elif j + 1 < len(intervals) and intervals[j+1][0] > newInterval[1]:
            solInt.append(newInterval[1])
            sol.append(solInt)
            return sol + intervals[j+1:]
          
sol = Solution()
# answer = sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
answer = sol.insert([[1,3],[6,9]], [2,5])

# answer = sol.insert([[1,3]], [2,5])
print(answer)
