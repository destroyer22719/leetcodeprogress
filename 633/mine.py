class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    squares = {}

    if (c**(1/2)).is_integer():
      return True

    for i in range(c//2+1):
      square = i**2

      squares[square] = True
      
      if square > c:
        break
    
    for square in squares:
      if c - square in squares:
        return True
    return False
  
sol = Solution()
a = sol.judgeSquareSum(5)
print(a)