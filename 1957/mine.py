class Solution:
  def makeFancyString(self, s: str) -> str:
    result = ""
    streak = 0

    for i in s:
      if result == "" or result[-1] != i:
        streak = 1
        result += i
      elif streak == 2:
        continue
      else:
        result += i
        streak += 1
    return result
  
