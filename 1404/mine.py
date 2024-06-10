class Solution:
  def numSteps(self, s: str) -> int:
    def divideTwo(num):
      return num[:-1]
    
    def addOne(num):
      num = list(num)
      for i in range(len(num) - 1, -1, -1):
        if num[i] == "0":
          num[i] = "1"
          return "".join(num)
        else:
          num[i] = "0"
      return "1" + "".join(num)
    
    def calculate(num):
      if num == "1":
        return 0
      if num[-1] == "0":
        return 1 + calculate(divideTwo(num))
      elif num[-1] == "1":
        return 1 + calculate(addOne(num))
    return calculate(s)
  
sol = Solution()
a = sol.numSteps("1")
print(a)