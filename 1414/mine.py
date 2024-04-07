class Solution:
  def fibonSeq(self, limit):
    result = [1, 1]

    n = 3
    while True:
      new = result[n-2] + result[n-3]

      result.append(new)
      n += 1
      if new >= limit:
        return result
      
  def findMinFibonacciNumbers(self, k: int) -> int:
    seq = self.fibonSeq(k)
    nums = 0
    currSum = 0

    if currSum == k:
      return 1

    n = -1

    while currSum < k:
      if (currSum + seq[n]) > k:
        n -= 1
      elif (currSum + seq[n] < k):
        nums += 1
        currSum += seq[n]
        n -= 1
      else:
        return nums + 1


sol = Solution()

minAmt = sol.findMinFibonacciNumbers(19)
print(minAmt)