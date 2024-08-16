class Solution:
  def isValid(self, s: str) -> bool:
    i = 0
    while len(s) > 0:
      if i == len(s):
        return False
      if s[i] == "]" and (i == 0 or s[i-1] != "["):
        return False
      elif s[i] == ")" and (i == 0 or s[i-1] != "("):
        return False
      elif (s[i] == "}" and ( i == 0 or s[i-1] != "{")):
        return False
      elif s[i] == "]" or s[i] == ")" or s[i] == "}":
        s = s[:i-1] + s[i+1:] 
        i -=1
      else:
        i += 1

    return s == ""
  
sol = Solution()
a = sol.isValid("()")
print(a)
