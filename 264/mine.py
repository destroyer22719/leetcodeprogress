class Solution:
  def nthUglyNumber(self, n: int) -> int:
    nums = []

    def isUglyNumber(n: int):
      # match = None
      # for prev in nums[::-1]:
      #   if (n / prev).is_integer():
      #     match = prev
      #     break
      
      # if match == 1:
      #   return False
      # if match != None:
      #   n /= match

      while (n/2).is_integer():
        n /= 2
      
      while (n/3).is_integer():
        n /= 3
      
      while (n/5).is_integer():
        n /= 5

      return n == 1
    

    count = 0
    i = 1
    while count != n:
      if isUglyNumber(i):
        count += 1
        nums.append(i)
      i += 1
    
    return nums[-1]
  
sol = Solution()

a = sol.nthUglyNumber(10)
print(a)