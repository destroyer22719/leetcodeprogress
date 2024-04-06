class Solution:
  def hammingWeight(self, n: int) -> int:
    
    remainder = n
    result = 0
    for i in range(32, -1, -1):
      if remainder >= 2**i:
        result += 1
        remainder -= 2**i
      if remainder == 0:
        break
    return result
  
sol = Solution()

print(sol.hammingWeight(2147483645))