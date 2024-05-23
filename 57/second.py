from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    sol = []

    if intervals == []:
      return [newInterval]
    
    n = len(intervals)
    for i, interval in enumerate(intervals):
      # these two if statements are mutually exclusive
      if interval[1] < newInterval[0]:
        sol.append(interval)
      if interval[0] > newInterval[1]:
        sol += [newInterval]
        sol += intervals[i:]
        return sol
      if (interval[0] <= newInterval[0] and newInterval[0] <= interval[1]) or (interval[0] <= newInterval[1] and newInterval[1] <= interval[1]):
        newInsert = [min(interval[0], newInterval[0]), None]

        for j in range(i, n):
          endInterval = intervals[j]

          if newInterval[1] < endInterval[0]:
            newInsert[1] = newInterval[1]
            sol.append(newInsert)
            sol += intervals[j:]
            return sol
          if newInterval[1] < endInterval[1]:
            newInsert[1] = endInterval[1]
            sol.append(newInsert)
            sol += intervals[j+1:]
            return sol
        newInsert[1] = max(newInterval[1], intervals[-1][1])
        sol += [newInsert]
        return sol
    return sol + [newInterval]

sol = Solution()

# answer = sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
# print(answer)

# answer = sol.insert([[1,3],[6,9]], [2,5])
# print(answer)

# answer = sol.insert([[1,2]], [3,4])
# print(answer)

# answer = sol.insert([[1,5]], [2,7])
# print(answer)

answer = sol.insert([[1,5]], [0,3])
print(answer)