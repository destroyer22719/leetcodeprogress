class Solution:
  def nthUglyNumber(self, n: int) -> int:
    q = [1,2,3,5]
    count = 0

    def binary_insert(n):
      nonlocal q
      if n < q[-1]:
        q.append(n)
        return


      left = 0
      right = len(q) - 1
      mid = (left + right) // 2

      while left <= right:
        mid = (left + right) // 2
        if q[mid-1] < n < q[mid] or mid == len(q) - 1:
          q = q[:mid] + [n] + q[mid:]
          return
        if q[mid] < n:
          left = mid + 1
        else:
          right = mid - 1

    while count != n:
      val = q.pop(0)

      count += 1
      if count == n:
        return val
      
      binary_insert(val*2)
      binary_insert(val*3)
      binary_insert(val*5)

sol = Solution()
a = sol.nthUglyNumber(10)
print(a)