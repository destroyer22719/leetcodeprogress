class Solution:
  def findComplement(self, num: int) -> int:
    first_one = False
    answer = 0
    for i in range(32, -1, -1):
      if 2**i <= num:
        if first_one == False:
          first_one = True
        num -= 2**i
      else:
        if first_one:
          answer += 2**i

    return answer
  
sol = Solution()
print(sol.findComplement(1))