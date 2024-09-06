from typing import List


class Solution:
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    stack = []

    while pushed != [] and popped != []:
      stack.append(pushed.pop(0))

      while stack != [] and popped != [] and stack[-1] == popped[0]:
        popped.pop(0)
        stack.pop()
      
      if pushed != [] and popped != []:
        break

      if popped[0] in stack:
        return False
    
    return True
  
sol = Solution()
a = sol.validateStackSequences([1,2,3,4,5],[4,3,5,1,2])
print(a)