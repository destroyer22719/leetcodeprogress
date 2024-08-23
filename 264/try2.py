class Solution:
  def nthUglyNumber(self, n: int) -> int:
    nums = {
      2: True,
      3: True,
      5: True
    }

    def isMagicNum(num):
      if num == 1:
        return True
      return num/3 in nums or num/2 in nums or num/5 in nums

    count = 0
    i = 1
    while True:
      if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        if isMagicNum(i):
          count += 1
          nums[i] = True

          if count == n:
            return i
      i += 1
    
sol = Solution()
a = sol.nthUglyNumber(10)
print(a)


