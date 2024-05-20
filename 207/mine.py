from typing import List

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    pres = { i: [] for i in range(numCourses)}

    for course, pre in prerequisites:
      pres[course].append(pre)

    traversed = { i: [] for i in range(numCourses)}

    visited = {}
    def dfs(course, root):
      if course in visited:
        return False
      
      if course != root:
        traversed[root].append(course)

      if pres[course] == []:
        return True
      
      visited[course] = True

      for p in pres[course]:
        if dfs(p, root) == False:
          return False
        
      del visited[course]
      pres[course] = []
      return True
    
    for c in  range(numCourses):
      if dfs(c, c) == False:
        return False
      for t in traversed[c]:
        pres[t] = []
      
    return True
  
sol = Solution()
answer = sol.canFinish(2, [[1,0],[0,1]])

print(answer)
  
    